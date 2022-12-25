from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name="loginpage"),
    path('get_user_details', views.getUserDetails, name="getUserDetails"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('doLogin', views.doLogin, name="doLogin"),

    path('themHS', views.themHS, name = 'themHS'),
    
    path('home/', views.homepage, name = "homepage"),
    path('danhsachlop/', views.dsLop, name = "dsLop"),
    path('chonnamhoc/', views.chonNamHoc, name = "chonNamHoc"),
    path('lapDSlop/', views.lapDSLop, name = "lapDS"),


]