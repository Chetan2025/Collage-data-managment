from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['section', 'name', 'roll_no', 'address', 'mobile', 'subject', 'cgpa']
