from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


admin.site.register(Student, StudentAdmin)