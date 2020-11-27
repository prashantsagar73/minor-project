from django.shortcuts import render
from django.http import HttpResponse
from .models import Events

# Create your views here.
def index(request):
    # return HttpResponse("This is events page")

    myposts = Events.objects.all()
    print(myposts)
    return render(request, 'events.html', {'myposts': myposts})

def blogpost (request, id):
    post = Events.objects.filter(post_id=id) [0]
    # print(post)
    return render(request, 'blogpost.html', {'post': post})



