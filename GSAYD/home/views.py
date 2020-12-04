from django.shortcuts import render, redirect,HttpResponse
from home.models import Contact
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
        # print(name,email,content,phone)
        # contact=Contact(name=name,email=email,phone=phone,content=content)
        # contact.save()
        if len(name)<2 or len(email)<3 or len(phone)<9 or len(content)<5:
            messages.error(request,'Please fill with correct details')
        else:
            contact= Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your message has been send.Thankyou for contacting us,we will be touch with you soon.')
    return render (request,'contact.html')    

def handelsignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        name= request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        sname = request.POST['sname']
        contactno = request.POST['contactno']

        # check for errorneous input
        # Prashant_sagar
        if len(username)>12:
            messages.error(request,"Username must be under 12 character")
            return redirect('home') 
        if not username.isalnum():
            messages.error(request,"Username contain only letters and number")
            return redirect('home') 
        if pass1 != pass2:
            messages.error(request,"Passworddo not match")
            return redirect('home')    
        # creating users
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.school_name = sname
        # myuser.contact_no = contactno
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')
    else: 
        return HttpResponse ('404 - Not Found')

    # Prashant sagar
def handellogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        # import authenticate
        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In as ")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials please try again.")
            return redirect('home')

    return HttpResponse ('404 - Not Found')

def handellogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

def fileuploader(request):
    return render(request,'fileuploader.html')
