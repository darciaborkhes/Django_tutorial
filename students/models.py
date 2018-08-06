from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    email =models.EmailField(unique = True)
    phone = models.CharField(max_length = 14)
    address = models.CharField(max_length = 220)
    skype = models.CharField(max_length = 20)
    courses = models.ManyToManyField(Course, related_name='courses', blank=True)


    def __str__(self):
        return self.name + " " + self.surname