from django.contrib import admin

# Register your models here.

from .models import Student, Subject, Age, ClassOfSchool, Mark

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Age)
admin.site.register(ClassOfSchool)
admin.site.register(Mark)
