from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *
from .forms import *

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .EmailBackEnd import EmailBackEnd
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def homepage(request):
    message = "This is temporary home page for our project"
    context = {'message': message}
    return render(request, 'studentManager/homepage.html', context)


def loginpage(request):
    context = {}
    return render(request, 'studentManager/loginpage.html', context)


@csrf_exempt
def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h3>Method Not Allowed</h3>")
    else:
        # return HttpResponse("account:" + request.POST.get('username')+ '-' + request.POST.get('password'))
        # user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = EmailBackEnd.authenticate(
            request, username=username1, password=password1)
        if user != None:
            login(request, user)
            # return HttpResponse("account:" + request.POST.get('username')+ '-' + request.POST.get('password'))
            return HttpResponseRedirect("home/")
        else:
            messages.error(request, "Invalid login details")
            return HttpResponseRedirect("/")


def getUserDetails(request):
    if request.user != None:
        return HttpResponse("USER: " + request.user.username + " user type: " + request.user.role)
    else:
        return HttpResponse("Please login first!")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

# def themHS(request):
#     context = {}
#     return render(request, 'studentManager/themHS.html', context)


def themHS(request):
    form = StudentForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            try:
                user = CustomUser.objects._create_user(
                    username=username, password=password, name=name,
                    role='3',
                    # dateOfBirth=datetime.strptime(dateOfBirth, '%Y-%m-%d', tzinfo=pytz.UTC ),
                    dateOfBirth=dateOfBirth,
                    sex=sex,
                    email=email,
                    address=address
                )

                student = Student(user=user)
                user.save()
                print(student)
                student.save()
                messages.success(request, "Thêm thành công")
            except:
                messages.error(request, "Không thể thêm")
        else:
            messages.error(request, "Dữ liệu không phù hợp")
    return render(request, 'studentManager/themHS.html', context=context)


def themHS_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:

        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        dob = request.POST.get("dateOfBirth")
        sex = request.POST.get("sex")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
                print('in-----------------------')
                print(username, name)
                try:
                    user = CustomUser.objects._create_user(
                        username=username, password=password, name=name,
                        dateOfBirth=datetime.strptime(dob, '%Y-%m-%d'),
                        # sex=sex,
                        role='3',  email=email, address=address)
                except:
                    messages.error(request, 'Thêm thất bại 0')
                    return HttpResponseRedirect("/themHS")

                user.save()
                student = Student(user=user)
                print(student)
                student.save()
                messages.success(request, 'Thêm thành công')
                return HttpResponseRedirect("/themHS")
        except:
            print('in-Thêm thất bại----------------------')
            print(username, name)
            messages.error(request, 'Thêm thất bại')
            return HttpResponseRedirect("/themHS")

    context = {}
    return render(request, 'studentManager/themHS.html', context)


def userProfile(request):
    context = {}
    return render(request, 'studentManager/userProfile.html', context)


# @allowed_users(allowed_roles=['Admin'])
def dsTaiKhoanHS(request):
    accountsStudent = Student.objects.all().order_by('user__name')
    formatDate = [a.user.dateOfBirth.strftime(
        "%d-%m-%y") for a in accountsStudent]
    accounts = zip(accountsStudent, formatDate)
    context = {
        'accounts': accounts,
    }
    return render(request, 'studentManager/dsTaikhoanHS.html', context=context)


# @allowed_users(allowed_roles=['Admin'])
def capNhatTKHS(request, account_id):
    account = get_object_or_404(Student, id=account_id)
    user = get_object_or_404(CustomUser, id=account.user.id)
    form = updateCustomUserForm(request.POST or None, instance=user)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            try:
                account = Student.objects.get(id=account.id)
                user = CustomUser.objects.get(id=account.user.id)
                user.username = username
                user.name = name
                user.dateOfBirth = dateOfBirth
                user.sex = sex
                user.email = email

                user.address = address
                user.save()
                messages.success(request, "Cập nhật thành công")
                #return redirect(to='dsTaiKhoanHS')
                return HttpResponseRedirect(reverse('dsTaiKhoanHS'))
            except:
                messages.error(request, "Không thể Không thể cập nhật")
        else:
            messages.error(request, "Dữ liệu không phù hợp")
    else:
        return render(request, "studentManager/capNhatHS.html", context)


semester = 2

# @login_required(login_url = 'login')

def dsLop(request):
    students = Student.objects.all()
    class_filter = ClassFilter(request.GET, queryset=students)
    students = class_filter.qs.order_by('user__name')
    format_date = [s.user.dateOfBirth.strftime("%d-%m-%y") for s in students]
    context = {
        'students': zip(students, format_date),
        'class_filter': class_filter,
    }

    return render(request, 'studentManager/dslop.html', context)


# @login_required(login_url='login')
def chonNamHoc(request):
    form = YearForm()
    age = Age.objects.all()
    context = {
        'form': form,
        'age': age
    }
    return render(request, 'studentManager/chonNamHoc.html', context)


@login_required(login_url='login')
def lapDSLop(request, pk):
    year = Age.objects.get(id=pk)
    student_list1 = []
    for student in Student.objects.all():
        for c in student.obj.all():
            if c.year == year:
                student_list1.append(student)
                break
    student_list2 = []
    for student in Student.objects.all():
        if student not in student_list1:
            student_list2.append(student)
    formatDate = [a.user.dateOfBirth.strftime(
        "%d-%m-%y") for a in student_list2]
    form = lapDSForm(request.POST, age_id=pk)
    if request.method == 'POST':
        usernames = request.POST.getlist('username_class')
        class_id = request.POST.get('classID')
        class_list = SchoolClass.objects.all()
        for obj in class_list:
            if obj.classID == class_id:
                studentsInClass = Student.objects.filter(
                    classOfSchool__classID=class_id)
                if obj.n_students >= (len(studentsInClass) + len(usernames)):
                    for username in usernames:
                        student = Student.objects.get(user__username=username)
                        student.classOfSchool.add(obj)
                        student.save()
                        for sub in Subject.objects.all():
                            for semester_mark in range(1, semester + 1):
                                mark = Mark()
                                mark.student = student
                                mark.subject = sub
                                mark.semester_mark = semester_mark
                                mark.markFifteen = 0
                                mark.markOne = 0
                                mark.markFinal = 0
                                mark.save()
                    messages.success(request, "Thêm thành công")
                    return redirect(reverse('lapDSLop', kwargs={'age_id': pk}))
                else:
                    messages.success(
                        request, "Số lượng học sinh vượt quá qui định")
    context = {
        'students': zip(student_list2, formatDate),
        'form': form,
    }
    return render(request, 'admin_template/lapDS.html', context=context)


def trungBinhMon(subject, student):
    for mark in Mark.objects.filter(student=student).filter(subject=subject):
        if mark.semester_mark == '1':
            avgMarks1 = round(
                (mark.markFifteen + 2 * mark.markOne + 3 * mark.markFinal) / 6, 2)
        else:
            avgMarks2 = round(
                (mark.markFifteen + 2 * mark.markOne + 3 * mark.markFinal) / 6, 2)
    return avgMarks1, avgMarks2

# @login_required(login_url='login')


def traCuuNamHoc(request):
    form = YearForm()
    age = Age.objects.all()
    context = {
        'form': form,
        'age': age
    }
    return render(request, 'studentManager/traCuuNamHoc.html', context)


# @allowed_users(allowed_roles=['Admin', 'Teacher'])
@login_required(login_url='login')
def traCuu(request):  # ,pk):
    '''year = Age.objects.get(id =pk)
    marks = Mark.objects.filter(subject__year= year)
    marksFilter = StudentInMarkFilter(request.GET, queryset=marks)
    marks = marksFilter.qs.order_by('student__user__name')
    students = []
    avgMarks1 = []
    avgMarks2 = []
    classOfSchool = []
    marks_in_year = marks
    students_in_year = set([mark.student for mark in marks_in_year])
    print(students_in_year)
    for student in students_in_year:
        students.append(student)
        subjects_in_year = set([mark.subject for mark in marks_in_year])
        m = [trungBinhMon(subject, student) for subject in subjects_in_year]
        s1 =0
        s2 = 0
        for i in m:
            s1+= i[0]
            s2 += i[1]
        avgMarks1.append(s1/len(m))
        avgMarks2.append(s2/len(m))
        for c in student.classOfSchool.all():
            if c.year == year:
                classOfSchool.append(c)
                break

    marks = zip(students, classOfSchool, avgMarks1, avgMarks2)
    
    context = {
        'marks': marks,
        'marksFilter': marksFilter
    }'''
    context = {}
    return render(request, 'studentManager/traCuu.html', context)
