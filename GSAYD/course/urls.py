
from django.contrib import admin
from django.urls import path,include
from course import views
urlpatterns = [
    path('', views.course, name='course'),

]