from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .filters import *

# Create your views here.
# @login_required(login_url = 'login')
# def showClasses(request):
#     students = Student.objects.all()
#     class_filter = classFilter(request.GET, queryset=students)
#     students = class_filter.qs.order_by('user__name')
#     format_date = [s.user.dateOfBirth.strftime("%d-%m-%y") for s in students]
#     context = {
#         'students': zip(students,format_date),
#         'class_filter': class_filter,
#     }
#     return render(request, ' .html', context)