from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def club(request):
    # return HttpResponse("Thsi is club page")
    return render(request,'club.html')