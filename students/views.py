from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Student
from django.views.generic.list import ListView
from .forms import StudentModelForm
from django.contrib import messages
from django.urls import reverse_lazy

class StudentListView(ListView):

    model = Student
    context_object_name = 'students_list'

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', '')
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs




# Create your views here.
# def students_view(request):
#
#     course_id = request.GET.get('course_id','')
#     if course_id:
#         students_list = Student.objects.filter(courses__id=course_id)
#
#     else:
#         students_list = Student.objects.all()
#
#
#     return render(request, 'students/student_list.html', {'students_list':students_list})

class StudentDetailView(DetailView):
    context_object_name = 'student'
    model = Student
    template_name = 'students/detail.html'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/student_add.html'
    success_url = reverse_lazy('students:student_list')

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', '')
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs


    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        messages.success(self.request, 'The student has been added')
        return response


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/student_edit.html'
    success_url = reverse_lazy('students:student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        messages.success(self.request, 'The student has been saved')
        return response

class StudentDeleteView(DeleteView):
    model = Student
    form_class = StudentModelForm
    template_name = 'students/student_remove.html'
    success_url = reverse_lazy('students:student_list')
