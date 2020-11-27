from django.shortcuts import render
from django.http import HttpResponse
from .models import Club


# Create your views here.
def index(request):
    # return HttpResponse("This is events page")
    myposts = Club.objects.all()
    print(myposts)
    return render(request, 'club.html', {'myposts': myposts})

def clubpost (request, id):
    post = Club.objects.filter(post_id=id) [0]
    # print(post)
    return render(request, 'clubpost.html', {'post': post})