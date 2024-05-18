from django.shortcuts import render,redirect
from .form import create_students_form
from .models import students,collage,student_message
from django.contrib.auth import authenticate,login,logout ,models
from django.contrib.auth.models import User
from django.contrib.messages import error
# Create your views here.
def loginUSer(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    if request.method == "POST":
        try:
            user=User.objects.get(username=username)
        except:
            error(request,"invalid username ")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            error(request,"invalid username ")
    return render(request,"login_register.html")
def logoutUser(request):
    logout(request)
    return redirect("login-user")
def registerUser(request):

    return render(request,"login_register.html")
def home(request):    
    students_obj=students.objects.all()
    content={"students":students_obj}
    return render(request,"home.html",content)
def student_data(request,pk):
    student_obj=students.objects.get(id=pk)
    student_msg=student_obj.student_message_set.all()
    content={"student_obj":student_obj,"student_msg":student_msg}
    return render(request,"student_data.html",content)
def student_message(request):
    pass
def create_students(request):
    form=create_students_form()
    if request.method == 'POST':
        form=create_students_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
            
    content={"form":form}
    return render(request,"create_student.html",content)
