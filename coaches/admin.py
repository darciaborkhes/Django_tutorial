from django.contrib import admin
from .models import Coach
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import User
from courses.models import Course


# class CourseAssistantInline(admin.StackedInline):
#     model = Course
#     fk_name = 'assistant'
#
# class CourseCoachInline(admin.StackedInline):
#     model = Course
#     fk_name = 'coach'
# Register your models here.
class CoachAdmin(admin.ModelAdmin):
    list_display = ('user','gender', 'skype', 'description', 'coach_courses', 'assistant_courses' )
    list_filter = ('user__is_staff', )

    def coach_courses(self, obj):
        return self.coach_courses

    def assistant_courses(self, obj):
        return self.assistant_courses
    # inlines = (CourseAssistantInline, CourseCoachInline, )
class CoachInline(admin.StackedInline):
    model = Coach

class UserAdmin(BaseUserAdmin):
    # list_display = ('first_name', 'last_name','username', 'email')
    inlines = (CoachInline, )



admin.site.unregister(User)
admin.site.register(Coach, CoachAdmin)
admin.site.register(User, UserAdmin)