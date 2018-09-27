from django.db import models
from django import forms
from coaches.models import Coach

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 100)
    short_description = models.CharField(max_length = 220)
    description = models.TextField()
    coach = models.ForeignKey(Coach, blank=True, null=True, related_name='coach_courses', on_delete = models.CASCADE)
    assistant = models.ForeignKey(Coach, blank=True, null=True, related_name = 'assistant_courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    subject = models.CharField(max_length = 100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject

