from django import forms
from .models import CustomUser, Student, Professor

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'user_id')  # Use ID field instead of email field

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('user', 'dept_name', 'tot_cred')  # Include fields from Student model

class ProfessorCreationForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('user', 'dept_name', 'salary')  # Include fields from Professor model
