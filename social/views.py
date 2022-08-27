from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, study, Payment

# Create your views here.
def index(request):
    return render(request, 'social/index.html')

def register(request):
    if request.method=="POST":
        username = request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        password= request.POST['password']
        password1= request.POST['password1']

        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=fname, last_name=lname, email=email, password = password)
                user.save()
                return redirect('login')
    return render(request, 'social/register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'social/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
def contact(request):
    return render(request, 'social/contact.html')

@login_required
def profile(request):
    return render(request, 'social/profile.html')

def causes(request):
    return render(request, 'social/causes.html')

def about(request):
    return render(request, 'social/about.html')


def donate(request):
    return render(request, 'social/donate.html')

def members(request):
    return render(request, 'social/members.html')

def volunteering(request):
    return render(request, 'social/volunteering.html')





