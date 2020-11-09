from django.shortcuts import render, HttpResponse, redirect
from club.models import Club


# Create your views here.
def club(request):
    allPosts = Club.objects.all()
    # print(allPosts)
    context = { 'allPosts' : allPosts}
    return render(request,'club.html', context)


def clubpost(request):
    return  render(request,'clubpost.html')