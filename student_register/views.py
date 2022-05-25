from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from student_register.forms import StudentForm
from .models import Student
# Create your views here.


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_register/student_form.html'
    success_url = reverse_lazy('list')


class StudentListView(ListView):
    model = Student
    template_name = 'student_register/student_list.html'
    context_object_name = 'students'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_register/student_update.html'
    success_url = reverse_lazy('list')
    


class StudentDeleteView(DeleteView):
    model= Student
    template_name = 'student_register/student_delete.html'
    success_url = reverse_lazy('list')