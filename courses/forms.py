
from django import forms
from .models import Course, Lesson

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['short_description']
class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['course']