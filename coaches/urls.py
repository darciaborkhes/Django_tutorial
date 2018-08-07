from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'coaches'
urlpatterns = [
    # url(r'^$', views.HomeView.as_view(), name = 'course_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.CoachView.as_view(), name='coach_details'),]