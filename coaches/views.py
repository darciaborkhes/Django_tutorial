from django.shortcuts import render
from django.views import generic
from .models import Coach

# Create your views here.
class CoachView(generic.DetailView):
    context_object_name = 'coach'
    template_name = 'coaches/coach_details.html'
    def get_queryset(self):
        return Coach.objects.all()