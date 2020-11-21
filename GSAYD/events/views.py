from django.shortcuts import render, HttpResponse,redirect
from events.models import Events

# Create your views here.
def events(request):
    # return HttpResponse("This is events page")
    allPosts = []
    context = {'allPosts': allPosts}
    return render(request, "events.html",context)

