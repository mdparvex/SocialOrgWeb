from re import U
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Donate, Event, Contact

# Create your views here.
def index(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    argentDonation = Event.objects.get(event_name='POOR IN SOCITY NEED YOUR HELP')
    progress = round(((int(argentDonation.ammount_raised)/50000)*100),2)
     
    contex = {
            'pr':pr, 
            'argentDonation':argentDonation,
            'progress':progress
        }
    return render(request, 'social/index.html', contex)

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
                return redirect('register')
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

        if (len(Uname) and len(email) and len(Uaddress) and len(Uphone) and len(Uprofession))<2:
            messages.info(request, 'Information wrong or any field is blank')
            return redirect('join')
        if Uphoto is None:
            messages.info(request, 'Photo must be upload')
            return redirect('join')

        p = Profile(user=user, name=Uname,email=email, address=Uaddress, phone=Uphone, proffesion=Uprofession, photo=Uphoto, comment=Ucomment)
        p.save()
        return redirect('join')
        
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    if pr is not None:
        return render(request, 'social/authuserprofile.html', {'pr':pr})
    
    
    return render(request, 'social/join.html')

@login_required
def donate(request):
    event = Event.objects.all()
    profile = Profile.objects.all().order_by('-total_donated')[:3]
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

        panding_num = len(Donate.objects.filter(user=request.user, varified=False).all())
        if panding_num>1:
            messages.info(request, 'Sorry you are not able to donate now, You have more than two panding donation, Contact with admin to confirm your previous donation !!!!!!')
            return redirect('donate')

        if (len(paymentway) and len(trxid) and len(ammount))<1 or date is None:
            messages.info(request, 'sorry, Any field is blank !!!!!!')
            return redirect('donate')

        for e in event:
            if e.event_name == request.POST['eventname']:
                event=Event.objects.get(event_name=e.event_name)
                event.ammount_raised = int(event.ammount_raised)+int(ammount)
        
        if pr is None:
            d= Donate(user=user, event=event, payment_way=paymentway, trxid=trxid, ammount=ammount, date=date)
            d.save()
            event.save()
            messages.info(request, 'Donation sucessfull !!!')
            return redirect('donate')
            
        pr.total_donated = int(pr.total_donated)+int(ammount)
        d= Donate(user=user, event=event, payment_way=paymentway, trxid=trxid, ammount=ammount, date=date)
        d.save()
        pr.save()
        event.save()
        messages.info(request, 'Donation sucessfull !!!')
        return redirect('donate')
    context={
        'pr':pr, 
        "event":event, 
        'profile':profile
        }

    return render(request, 'social/donate.html', context)

def members(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    userprof = Profile.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        userprof = Profile.objects.filter(name__icontains=search_term)
    
    context = {
        'pr':pr, 
        'userprof':userprof
        }
    return render(request, 'social/members.html', context)

def profile(request,uid):
    try:
        pr = Profile.objects.get(pk=uid)
    except:
        pr = None
    user=User.objects.get(username=pr.user)
    context = {
        'pr':pr, 
        'user':user
        }
    return render(request, 'social/profile.html', context)

def history(request, id):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    user = User.objects.get(pk=id)
    payment = Donate.objects.filter(user=user).order_by('-date')[:30]
    context = {
        'pr':pr, 
        'payment':payment ,
        'user':user
        }
    return render(request, 'social/history.html', context)

@login_required
def editprofile(request):
    pr = Profile.objects.get(user=request.user)
    if request.method=='POST':
        if request.FILES.get('image') !=None:
            image=request.FILES.get('image')
        else:
            image = pr.photo
        pr.name = request.POST['name']
        pr.email=request.POST['email']
        pr.address = request.POST['address']
        pr.phone = request.POST['phone']
        pr.profession = request.POST['proffession']
        pr.comment = request.POST['comment']
        pr.photo = image
        pr.save()
        return redirect('profile', uid=pr.id)
    return render(request, 'social/editprofile.html', {'pr':pr})
def causes(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    
    ammount1 = Event.objects.get(event_name='ORPHAN NEED YOUR HELP').ammount_raised
    ammount2 = Event.objects.get(event_name='POOR IN SOCITY NEED YOUR HELP').ammount_raised
    ammount3 = Event.objects.get(event_name='EID FASTIVE DONATION').ammount_raised
    ammount4 = Event.objects.get(event_name='MADRASHA NEED YOUR HELP').ammount_raised

    raised1 = round(((ammount1/50000)*100),2)
    raised2 = round(((ammount2/50000)*100),2)
    raised3 = round(((ammount3/50000)*100),2)
    raised4 = round(((ammount4/50000)*100),2)

    context = {
        'pr':pr,
        'ammount1':ammount1,
        'ammount2':ammount2,
        'ammount3':ammount3,
        'ammount4':ammount4,
        'raised1': raised1,
        'raised2': raised2,
        'raised3': raised3,
        'raised4': raised4,

        }
    return render(request, 'social/causes.html',context)

def about(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        pr = None
    return render(request, 'social/about.html', {'pr':pr})
def volunteering(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except:
        pr = None
    return render(request, 'social/volunteering.html', {'pr':pr})

def contact(request):
    try:
        pr = Profile.objects.get(user=request.user)
    except: #Profile.DoesNotExist
        pr = None
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        c = Contact(name=name, email=email, subject=subject, massege=message)
        c.save()
        if (len(name) and len(email) and len(subject) and len(message))<3:
            messages.info(request, 'Any field is blank or too small !!!')
            return redirect('contact')
        messages.info(request, 'Your massege has been sent !!!')
        return redirect('contact')

    return render(request, 'social/contact.html',{'pr':pr})





