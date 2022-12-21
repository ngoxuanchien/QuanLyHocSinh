from django.urls import path
from . import views

urlpatterns = [
    path('', views.tempHome, name = "home"),
    path('danhsachlop/', views.dsLop, name = "dsLop"),
]