from django.conf.urls import url
from . import views
from django.contrib import admin


app_name = 'quadratic'
urlpatterns = [
    url(r'quadratic/results/', views.quadratic_results, name='results'),

]