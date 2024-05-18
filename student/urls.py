from django.urls import path
from .views import *

urlpatterns=[
    path("login-user",loginUSer,name="login-user"),
    path("logout-user",logoutUser,name="logout-user"),
    path("register-user",registerUser,name="register-user"),
    path("",home,name="home"),
    path("create-student",create_students,name="create-students"),
    path("student-data/<str:pk>/",student_data,name="student-data"),


]