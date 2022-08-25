from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'social/index.html')
def volunteer(request):
    return render(request, 'social/volunteer.html')

def base(request):
    return render(request, 'social/base.html')
