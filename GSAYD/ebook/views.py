from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def ebook(request):
    return HttpResponse ("this is ebook page")
