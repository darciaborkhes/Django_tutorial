from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'courses'
urlpatterns = [
    url(r'add$', views.add_course, name = 'add'),
    url(r'edit/(?P<pk>[0-9]+)$', views.edit_course, name = 'edit'),
    url(r'remove/(?P<pk>[0-9]+)$', views.remove_course, name = 'remove'),
    url(r'^$', views.HomeView.as_view(), name='course_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/add_lesson$', views.LessonCreateView.as_view(), name='add_lesson'),





]