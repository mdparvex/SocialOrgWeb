from re import U
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Payment

# Create your views here.
def index(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    return render(request, 'social/index.html', {'pr':pr})

def register(request):
    if request.method=="POST":
        username = request.POST['username']
        password= request.POST['password']
        password1= request.POST['password1']

        if len(username)<4:
            messages.info(request, 'username is too sort')
            return redirect('register')
        if len(password)<7:
            messages.info(request, 'password must be at least 8 character')
            return redirect('register')

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password = password)
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
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    return render(request, 'social/contact.html',{'pr':pr})

@login_required
def join(request):

    if request.method=='POST':

        user= User.objects.get(username=request.user.username)
        Uname = request.POST['name']
        email=request.POST['email']
        Uaddress = request.POST['address']
        Uphone = request.POST['phone']
        Uprofession = request.POST['proffession']
        Ucomment = request.POST['comment']
        Uphoto = request.FILES.get('image')

        p = Profile(user=user, name=Uname,email=email, address=Uaddress, phone=Uphone, proffesion=Uprofession, photo=Uphoto, comment=Ucomment)
        p.save()
        return redirect('index')
    
    
    return render(request, 'social/join.html')

def profile(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    return render(request, 'social/profile.html', {'pr':pr})

def causes(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    return render(request, 'social/causes.html',{'pr':pr})

def about(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    return render(request, 'social/about.html', {'pr':pr})


def donate(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    return render(request, 'social/donate.html', {'pr':pr})

def members(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    userprof = Profile.objects.all()
    
    return render(request, 'social/members.html', {'pr':pr, 'userprof':userprof})

def volunteering(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    return render(request, 'social/volunteering.html', {'pr':pr})





