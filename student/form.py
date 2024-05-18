from django.forms import ModelForm
from .models import students,student_message
class create_students_form(ModelForm):
    class Meta:
        model=students
        fields='__all__'
