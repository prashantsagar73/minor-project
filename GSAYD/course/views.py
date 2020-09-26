from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def course (request):
    return HttpResponse ("This is course page")
