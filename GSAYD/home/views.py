from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home (request):
    return render (request,"Home.html")

def contact(request):
    # messages.success(request, 'Welcome to conatact.')
    if request.method == 'POST':
        name= request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        content =request.POST['content']
        print(name,email,content,phone)
        # contact=Contact(name=name,email=email,phone=phone,content=content)
        # contact.save()
        if len(name)<2 or len(email)<3 or len(phone)<9 or len(content)<5:
            messages.error(request,'Please fill with correct details')
        else:
            contact= Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your message has been send.Thankyou for contacting us,we will be touch with you soon.')
    return render (request,'contact.html')    