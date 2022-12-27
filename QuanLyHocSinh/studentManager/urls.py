from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name="loginpage"),
    path('get_user_details', views.getUserDetails, name="getUserDetails"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('doLogin', views.doLogin, name="doLogin"),

    path('themHS', views.themHS, name = 'themHS'),
    #path('themHS_save', views.themHS_save, name='themHS_save'),
    path("danhsachtaikhoanHS/", views.dsTaiKhoanHS, name='dsTaiKhoanHS'),
    path("danhsachtaikhoanHS/capnhat/<int:account_id>", views.capNhatTKHS, name='capNhatTKHS'),
    path("danhsachtaikhoanHS/delete/<int:account_id>", views.xoaTKHS, name='xoaTKHS'),
    
    path('profile', views.userProfile, name = 'userProfile'),
    
    path('home/', views.homepage, name = "homepage"),
    path('danhsachlop/', views.dsLop, name = "dsLop"),
    path('chonnamhoc/', views.chonNamHoc, name = "chonNamHoc"),
    path('lapDSlop/', views.lapDSLop, name = "lapDS"),

    path("tracuu/namhoc", views.traCuuNamHoc, name='traCuuNamHoc'),
    #path("tracuu/namhoc/namhoc_<int:age_id>", views.traCuu, name='traCuu'),
    path("tracuu/namhoc/", views.traCuu, name='traCuu'),
]