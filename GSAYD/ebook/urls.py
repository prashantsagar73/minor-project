
from django.contrib import admin
from django.urls import path,include
from ebook import views
urlpatterns = [
    path('', views.ebook, name='ebook'),

]