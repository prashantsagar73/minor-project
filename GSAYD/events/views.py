from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def events(request):
    return HttpResponse("events")
