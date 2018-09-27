from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_date']

# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)