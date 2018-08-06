from django.shortcuts import render
from django.views import generic
from .models import Course

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

