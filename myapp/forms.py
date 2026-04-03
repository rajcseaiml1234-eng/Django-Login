from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email', 'required': True}),
        }