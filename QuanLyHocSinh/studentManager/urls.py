from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name="loginpage"),
    path('get_user_details', views.getUserDetails, name="getUserDetails"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('doLogin', views.doLogin, name="doLogin"),

    path('themHS', views.themHS, name='themHS'),
    path("danhsachtaikhoanHS/", views.dsTaiKhoanHS, name='dsTaiKhoanHS'),
    path("danhsachtaikhoanHS/capnhat/<int:account_id>",
         views.capNhatTKHS, name='capNhatTKHS'),
    path("danhsachtaikhoanHS/delete/<int:account_id>",
         views.xoaTKHS, name='xoaTKHS'),

    path('capnhattaikhoan/', views.capNhatTaiKhoan, name='capNhatTaiKhoan'),
    path('profile', views.userProfile, name='userProfile'),

    path('home/', views.homepage, name="homepage"),
    path('danhsachlop/', views.dsLop, name="dsLop"),
    path('chonnamhoc/', views.chonNamHoc, name="chonNamHoc"),
    path('lapDSlop/<int:pk>', views.lapDSLop, name="lapDS"),

    path("tracuu/namhoc/", views.traCuuNamHoc, name='traCuuNamHoc'),
    path("tracuu/namhoc/namhoc_<int:pk>", views.traCuu, name='traCuu'),

    # path("tracuu/namhoc/", views.traCuu, name='traCuu'),
    path('monHoc', views.monHoc, name='monHoc'),
    path('markForm', views.mark_form, name='markForm'),
    path('updateMark/<str:pk>/', views.update_mark, name='updateMark'),
    path('deleteMark/<str:pk>/', views.delete_mark, name='deleteMark'),
    path("baoCao", views.baoCao, name='baoCao'),
    path("caiDat", views.Setting, name='caiDat'),
]
