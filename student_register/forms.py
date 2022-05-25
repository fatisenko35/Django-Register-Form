from django import forms
from django.forms import fields
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'Full_Name' : forms.TextInput(attrs={'class': 'form-control'}),
            'Mobile' : forms.NumberInput(attrs={'class': 'form-control'}),
            'Email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'Gender' : forms.Select(attrs={'class': 'form-control'}),
            'Student_Number' : forms.NumberInput(attrs={'class': 'form-control'}),
            'Path' : forms.Select(attrs={'class': 'form-control'}),
        }