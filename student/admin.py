from django.contrib import admin
from .models import students,collage,teachers,student_message

admin.site.register(collage)
admin.site.register(students)
admin.site.register(teachers)
admin.site.register(student_message)    


