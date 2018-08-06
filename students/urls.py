from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'students'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.students_view, name = 'student_list' ),


]