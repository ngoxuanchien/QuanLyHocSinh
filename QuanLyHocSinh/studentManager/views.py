from django.shortcuts import render
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
        #return HttpResponse("account:" + request.POST.get('username')+ '-' + request.POST.get('password'))
        #user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username=username1, password=password1)
        if user!=None:
            login(request,user)
            #return HttpResponse("account:" + request.POST.get('username')+ '-' + request.POST.get('password'))
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


# @login_required(login_url = 'login')
def dsLop(request):
    # students = Student.objects.all()
    # class_filter = ClassFilter(request.GET, queryset=students)
    # students = class_filter.qs.order_by('user__name')
    # format_date = [s.user.dateOfBirth.strftime("%d-%m-%y") for s in students]
    # context = {
    #     'students': zip(students,format_date),
    #     'class_filter': class_filter,
    # 
    context = {}
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
