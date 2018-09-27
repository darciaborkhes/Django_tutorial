from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'students'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='detail'),
    url(r'^add$', views.StudentCreateView.as_view(), name='student_add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.StudentUpdateView.as_view(), name='student_edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.StudentDeleteView.as_view(), name='student_edit'),
    url(r'$', views.StudentListView.as_view(), name = 'student_list' ),


]