from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'students'
urlpatterns = [
    url(r'^$', views.students_view, name = 'student_list'),

]