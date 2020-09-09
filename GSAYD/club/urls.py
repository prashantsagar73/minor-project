
from django.contrib import admin
from django.urls import path,include
from club import views
urlpatterns = [
    path('', views.club, name='club'),

]