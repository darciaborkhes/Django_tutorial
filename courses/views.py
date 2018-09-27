from django.shortcuts import render, redirect
from django.views import generic
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
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


class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonModelForm
    template_name = 'courses/add_lesson.html'
    success_url = reverse_lazy('courses:detail')



    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The lesson has been added')
        return response


# def add_lesson(request, pk):
#     course_obj = Course.objects.get(id=pk)
#     if request.method == 'POST':
#         lesson_form = LessonModelForm(request.POST)
#         if lesson_form.is_valid():
#             instance = lesson_form.save(commit=False)
#             instance.course = course_obj
#             lesson_form.save()
#             messages.success(request, '{} has been successfully added'.format(instance.subject))
#             return redirect('/courses/{}'.format(pk))
#     else:
#         lesson_form = LessonModelForm()
#     return render(request, 'courses/add_lesson.html', {'lesson_form':lesson_form})

def edit_course(request, pk):
    course_obj = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST,instance=course_obj)
        if form.is_valid():
            course_obj = form.save()
            messages.success(request, '{} has been successfully saved'.format(course_obj.name))
            return redirect('/courses/{}'.format(pk))
    else:
        form = CourseModelForm(instance=course_obj)
        return render(request, 'courses/edit_course.html', {'form': form})

def remove_course(request,pk):
    course_obj = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course_obj)
        if form.is_valid():
            course_obj.delete()
            messages.success(request, '{} was successfully deleted'.format(course_obj.name))
            return redirect('/courses/')
    else:
        form = CourseModelForm(instance=course_obj)
        return render(request, 'courses/remove_course.html', {'form': form})
