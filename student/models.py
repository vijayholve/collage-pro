from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class collage(models.Model):
    collageName=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    city=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.collageName
class teachers(models.Model):
    teachersName=models.CharField(max_length=20)
    salary=models.CharField(max_length=10)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    collage=models.ForeignKey(collage,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.teachersName
class students(models.Model):
    studentName=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    participants=models.ManyToManyField(User,related_name="participants")
    collage=models.ForeignKey(collage,on_delete=models.SET_NULL,null=True,blank=True)
    teachers=models.ForeignKey(teachers,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.studentName
    
    
class student_message(models.Model):
    msg=models.TextField(max_length=20,blank=True,null=True)
    students=models.ForeignKey(students,on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.msg
    