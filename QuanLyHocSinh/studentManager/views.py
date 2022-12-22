from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *

def homepage(request):
    message = "This is temporary home page for our project"
    context = {'message': message}
    return render(request, 'studentManager/homepage.html', context)


# Create your views here.
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