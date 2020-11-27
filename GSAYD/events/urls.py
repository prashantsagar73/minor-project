
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.index, name='events'),
    path("blogpost/<int:id>", views.blogpost, name="BlogPost")

]