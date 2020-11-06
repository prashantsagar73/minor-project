
from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('signup', views.handelsignup, name='handelsignup'),  
    path('login', views.handellogin, name='handellogin'),  
    path('logout', views.handellogout, name='handellogout')  

]