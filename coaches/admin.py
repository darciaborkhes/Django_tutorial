from django.contrib import admin
from .models import Coach
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import User

# Register your models here.
class CoachAdmin(admin.ModelAdmin):
    list_display = ('user','gender', 'skype', 'description')
    list_filter = ('staff_status', )

class UserAdmin(BaseUserAdmin):
    list_display = ('first_name', 'last_name','username', 'email')


admin.site.unregister(User)
admin.site.register(Coach, CoachAdmin)
admin.site.register(User, UserAdmin)