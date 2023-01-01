from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, ClassOfSchool, Subject, Mark, Age
from .form import *
from django.db import models
from django.db.models import Q
from django.contrib import messages
from .filter import *


# Create your views here.
def diemTrungBinhMon(student, subject):
    avgMarks1 = avgMarks2 = 0
    for mark in Mark.objects.filter(student=student).filter(subjects__name=subject):
        if mark.semester_mark == '1':
            avgMarks1 = (mark.markFifteen + 2 *
                         mark.markOne + 3 * mark.markFinal) / 6
        else:
            avgMarks2 = (mark.markFifteen + 2 *
                         mark.markOne + 3 * mark.markFinal) / 6

    # print(avgMarks1, avgMarks2)
    return avgMarks1, avgMarks2


def diemTrungBinhHocKy(student, year):
    if year == '' or year == None:
        subjects = Subject.objects.all()
    else:
        subjects = Subject.objects.filter(year__year=year)
    # print(subjects)
    avgMarks1 = avgMarks2 = 0
    for subject in subjects:
        temp = diemTrungBinhMon(student, subject.name)
        avgMarks1 += temp[0]
        avgMarks2 += temp[1]

    if len(subjects) != 0:
        avgMarks1 = round(avgMarks1 / len(subjects), 2)
        avgMarks2 = round(avgMarks2 / len(subjects), 2)
        return avgMarks1, avgMarks2

    return 0, 0


@ login_required(login_url='login')
def list_student(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    students = Student.objects.all().order_by('name')
    # classes = ClassOfSchool.objects.all()
    classFilter = ClassFilter(request.GET, queryset=students)
    students = classFilter.qs.order_by('name')
    stt = []
    listStudent = []
    avg1 = []
    avg2 = []

    students = students.filter(Q(name__icontains=q))
    # print(classFilter.form)
    year = request.GET.get('year')

    i = 0
    for st in students:
        i += 1
        listStudent.append(st)
        stt.append(i)
        tb1, tb2 = diemTrungBinhHocKy(st, year)
        avg1.append(tb1)
        avg2.append(tb2)

    students = zip(stt, listStudent, avg1, avg2)
    context = {
        'classFilter': classFilter,
        'students': students
    }
    return render(request, 'base/student.html', context=context)


@ login_required(login_url='login')
def addStudent(request):
    lops = ClassOfSchool.objects.all()
    form = StudentForm()
    years = Age.objects.all()
    if request.method == 'POST':
        button = request.POST.get('button')
        # print(button)
        if (button != "Cancel"):

            # year = Age.objects.filter(year=request.POST.get('year')).first()

            # print(request.POST.get('classOfSchool'))

            classschool = ClassOfSchool.objects.filter(
                id=request.POST.get('classOfSchool')).first()

            # try:
            Student.objects.create(
                name=request.POST.get('name'),
                dateOfBirth=request.POST.get('dateOfBirth'),
                sex=request.POST.get('sex'),
                address=request.POST.get('address'),
                email=request.POST.get('email'),
                classOfSchool=classschool
                # year=classschool.year
            )
            messages.success(request, "Thêm thành công")
            # return redirect('list_student_filter', year_id=classschool.year.id)
            # except:
            #     messages.error(request, "không thể thêm")
            #     return redirect('addStudent')

        return redirect('list_student')

    context = {'form': form, 'lops': lops, 'years': years}
    return render(request, 'base/addStudent.html', context)


@ login_required(login_url='login')
def deleteStudent(request, pk):
    studentt = Student.objects.get(id=pk)
    # year = studentt.year

    studentt.delete()

    return redirect('list_class')


@ login_required(login_url='login')
def student_form(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=student)
    # lops = ClassOfSchool.objects.all()
    # years = Age.objects.all()
    # print(form)

    context = {
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            address = form.cleaned_data.get('address')
            email = form.cleaned_data.get('email')
            classOfSchool = form.cleaned_data.get('classOfSchool')

            st = Student.objects.get(id=student.id)
            st.name = name
            st.dateOfBirth = dateOfBirth
            st.sex = sex
            st.address = address
            st.email = email
            st.classOfSchool = classOfSchool
            st.save()
            return redirect('list_class')

        # print(form.name)

        # if form.is_valid():

    return render(request, 'base/addStudent.html', context)


@ login_required(login_url='login')
def list_class(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    students = Student.objects.all().order_by('name')
    classFilter = ClassFilter(request.GET, queryset=students)
    students = classFilter.qs.order_by('name')
    students = students.filter(Q(name__icontains=q))
    formatDate = [a.dateOfBirth.strftime("%d-%m-%Y") for a in students]
    stt = []
    i = 0
    for a in students:
        i += 1
        stt.append(i)

    students = zip(stt, students, formatDate)
    context = {
        'classFilter': classFilter,
        'students': students,
        'siso': i,
    }
    return render(request, 'base/classSchool.html', context)


@ login_required(login_url='login')
def list_subject(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    marks = Mark.objects.all()
    markFilter = MarkFilter(request.GET, queryset=marks)
    # print(markFilter.form)
    marks = markFilter.qs
    marks = marks.filter(Q(student__name__icontains=q))

    stt = []
    i = 1
    for mark in marks:
        stt.append(i)
        i += 1

    marks = zip(stt, marks)
    context = {
        'marks': marks,
        'markFilter': markFilter,
    }
    return render(request, 'base/subject.html', context)


@ login_required(login_url='login')
def mark_form(request):
    form = MarkForm()

    context = {
        'form': form
    }

    if request.method == 'POST':
        if request.POST.get('button') == 'SAVE':

            subjects = Subject.objects.filter(
                id=request.POST.get('subjects')).first()
            student = Student.objects.filter(
                id=request.POST.get('student')).first()
            Mark.objects.create(
                subjects=subjects,
                student=student,
                markFifteen=request.POST.get('markFifteen'),
                markOne=request.POST.get('markOne'),
                markFinal=request.POST.get('markFinal'),
                semester_mark=request.POST.get('semester_mark'),
            )
            return redirect('list_subject')

    return render(request, 'base/markForm.html', context)


@ login_required(login_url='login')
def update_mark(request, pk):
    mark = Mark.objects.get(id=pk)
    form = MarkForm(request.POST or None, instance=mark)

    if request.method == 'POST':
        if form.is_valid():
            student = form.cleaned_data.get('subjects')
            objects = form.cleaned_data.get('student')
            markFifteen = form.cleaned_data.get('markFifteen')
            markOne = form.cleaned_data.get('markOne')
            markFinal = form.cleaned_data.get('markFinal')
            semester_mark = form.cleaned_data.get('semester_mark')

            st = Mark.objects.get(id=mark.id)
            st.student = Student.objects.get(id=student.id)
            st.objects = objects
            st.markFifteen = markFifteen
            st.markOne = markOne
            st.markFinal = markFinal
            st.semester_mark = semester_mark
            st.save()
            return redirect('list_subject')

    context = {
        'form': form
    }
    return render(request, 'base/markForm.html', context)


@ login_required(login_url='login')
def delete_mark(request, pk):
    mark = Mark.objects.get(id=pk)
    mark.delete()
    return redirect('list_subject')
