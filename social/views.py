from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'social/index.html')

def register(request):
    return render(request, 'social/register.html')

def login(request):
    return render(request, 'social/login.html')

def contact(request):
    return render(request, 'social/contact.html')

def causes(request):
    return render(request, 'social/causes.html')

def about(request):
    return render(request, 'social/about.html')

def profile(request):
    return render(request, 'social/profile.html')

def donate(request):
    return render(request, 'social/donate.html')

def members(request):
    return render(request, 'social/members.html')

def volunteering(request):
    return render(request, 'social/volunteering.html')

def base(request):
    return render(request, 'social/base.html')




