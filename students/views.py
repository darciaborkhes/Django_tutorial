from django.shortcuts import render
from django.views import generic
from .models import Student





# Create your views here.
def students_view(request):

    course_id = request.GET.get('course_id','')
    if course_id:
        students_list = Student.objects.filter(courses__id=course_id)

    else:
        students_list = Student.objects.all()


    return render(request, 'students/student_list.html', {'students_list':students_list})

class DetailView(generic.DetailView):
    context_object_name = 'student'
    model = Student
    template_name = 'students/detail.html'
