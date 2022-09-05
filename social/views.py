from re import U
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Payment, Event

# Create your views here.
def index(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
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
    except: #Profile.DoesNotExist
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
        
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    if pr is not None:
        return render(request, 'social/profile.html', {'pr':pr})
    
    
    return render(request, 'social/join.html')

def causes(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    return render(request, 'social/causes.html',{'pr':pr})

def about(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None


    return render(request, 'social/about.html', {'pr':pr})


def donate(request):
    event = Event.objects.all()
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    if request.method=='POST':
        user = User.objects.get(username=request.user.username)
        paymentway = request.POST['paymentway']
        trxid = request.POST['trxid']
        ammount = request.POST['ammount']
        date = request.POST['date']

        for e in event:
            if e.event_name == request.POST['eventname']:
                event=Event.objects.get(event_name=e.event_name)
                event.ammount_raised = int(event.ammount_raised)+int(ammount)
        pr.total_donated = int(pr.total_donated)+int(ammount)
        d= Payment(user=user, event=event, payment_way=paymentway, trxid=trxid, ammount=ammount, date=date)
        d.save()
        pr.save()
        event.save()
        messages.info(request, 'Donation sucessfull !!!')
        return redirect('donate')
        

    return render(request, 'social/donate.html', {'pr':pr, "event":event})

def members(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    userprof = Profile.objects.all()
    
    return render(request, 'social/members.html', {'pr':pr, 'userprof':userprof})

def profile(request,uid):
    try:
        pr = Profile.objects.get(pk=uid)
    except:
        pr = None
    user=User.objects.get(username=pr.user)
    return render(request, 'social/profile.html', {'pr':pr, 'user':user})

def history(request, id):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    user = User.objects.get(pk=id)
    payment = Payment.objects.filter(user=user)
    return render(request, 'social/history.html', {'pr':pr, 'payment':payment ,'user':user})

def volunteering(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    return render(request, 'social/volunteering.html', {'pr':pr})





