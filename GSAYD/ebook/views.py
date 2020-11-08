from django.shortcuts import render, HttpResponse,redirect
from .models import Pdf
# Create your views here.
def ebook(request):

    return render (request,'ebook.html')