from django.contrib import admin
from .models import Course, Lesson
from students.models import Student
# Register your models here.



# class CourseStudentInline(admin.TabularInline):
#     model = Course.students.through
#     extra = 1
#
# class StudentAdmin(admin.ModelAdmin):
#     inlines = [CourseStudentInline]
#
# # class StudentAdmin(admin.ModelAdmin):
# #     pass

# admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
# admin.site.register(StudentAdmin, CourseStudentInline)
admin.site.register(Lesson)



