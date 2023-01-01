from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *   
# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(SchoolClass)
admin.site.register(Age)
admin.site.register(Subject)
# admin.site.register(CustomUser)
