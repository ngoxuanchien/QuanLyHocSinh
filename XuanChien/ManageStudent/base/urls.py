from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.loginPage, name="login"),

    # path('', views.home, name="home"),
    path('list_student', views.list_student, name="list_student"),
    path('addStudent', views.addStudent, name="addStudent"),
    path('deleteStudent/<str:pk>/', views.deleteStudent, name="deleteStudent"),


    path('student_form/<str:pk>/', views.student_form, name="student_form"),
    path('list_class', views.list_class, name="list_class"),
    path('list_subject', views.list_subject, name="list_subject"),
    path('addMark', views.mark_form, name="addMark"),
    path('updateMark/<str:pk>/', views.update_mark, name="updateMark"),
    path('deleteMar/<str:pk>/', views.delete_mark, name="deleteMark"),
]
