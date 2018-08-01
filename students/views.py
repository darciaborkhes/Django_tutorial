from django.shortcuts import render
from django.views import generic
from .models import Student





# Create your views here.
def students_view(request):
    # print(request.GET)

    course_id = request.GET.get('course_id','')
    print(course_id)
    if course_id:
        students_list = Student.objects.filter(courses__id=course_id)
    else:
        students_list = Student.objects.all()
#     #
#     #     students_list = Student.objects.filter(courses_id=val)
#     #     print('No')
#     # except:
#     #     students_list = Student.objects.all()
#     #     print('All')
#     # print(students_list)
    return render(request, 'students/student_list.html', {'student_list': students_list,})
#     return Student.objects.all()

# class StudentView(generic.ListView):
#     template_name = 'student_list.html'
#     context_object_name = 'student_list'
#     def get_queryset(self):
#         try:
#             key, val = self.get.GET.items()
#             students_list = Student.objects.filter(courses_id=val)
#         except:
#             students_list = Student.objects.all()
#         return students_list