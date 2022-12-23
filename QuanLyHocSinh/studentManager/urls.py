from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name="loginpage"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('home/', views.homepage, name = "homepage"),
    path('danhsachlop/', views.dsLop, name = "dsLop"),
]