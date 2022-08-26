from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'social/index.html')

def register(request):
    return render(request, 'social/register.html')

def login(request):
    return render(request, 'social/login.html')

def profile(request):
    return render(request, 'social/profile.html')

def donate(request):
    return render(request, 'social/donate.html')

def volunteer(request):
    return render(request, 'social/volunteer.html')

def base(request):
    return render(request, 'social/base.html')




