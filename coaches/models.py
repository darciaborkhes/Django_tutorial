from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30,null= True)
    email = models.EmailField(max_length=30,null = True)
    date_of_birth = models.DateField(blank = True, null = True)
    gender = models.CharField(max_length = 1, choices = (('M', 'Male'),('F', 'Female')))
    phone = models.CharField(max_length = 14, blank = True, null=True)
    address = models.CharField(max_length = 20, blank = True, null=True)
    skype = models.CharField(max_length = 20, blank = True, null=True)
    description =models.TextField(max_length = 2000, blank= True, null=True)
    staff_status = models.BooleanField(default=False)
    position = models.CharField(max_length=1, choices= (('T', 'Trainer'), ('A', 'Assistant')), null=True)


    def __str__(self):
        return self.user.username

