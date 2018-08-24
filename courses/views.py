from django.shortcuts import render, redirect
from django.views import generic
from .models import Course, Lesson
from django import forms
from django.contrib import messages
# Create your views here.
class HomeView(generic.ListView):
    context_object_name = 'all_courses_list'
    template_name = 'courses/course_list.html'
    def get_queryset(self):
        return Course.objects.all()

class DetailView(generic.DetailView):
    context_object_name = 'course'
    model = Course
    template_name = 'courses/detail.html'


class ContactView(generic.TemplateView):
    template_name = 'courses/contact.html'


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['short_description']
class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['order']

def add_course(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, '{} has been successfully added'.format(instance.name))
            return redirect('/courses/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form':form})

def add_lesson(request, pk):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, '{} has been successfully added'.format(instance.name))
            return redirect('/courses/{}'.format(pk))
    else:
        form = LessonModelForm()
    return render(request, 'courses/add_lesson.html', {'form':form})