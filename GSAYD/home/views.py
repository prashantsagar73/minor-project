from django.shortcuts import render
from home.models import Contact

# Create your views here.
def home (request):
    return render (request,"Home.html")

def contact(request):
    if request.method == 'POST':
        name= request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        content =request.POST['content']
        print(name,email,content,phone)
        contact=Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
    return render (request,'contact.html')    