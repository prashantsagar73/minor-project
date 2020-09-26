from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def ebook(request):
    return render (request,'ebook.html')
