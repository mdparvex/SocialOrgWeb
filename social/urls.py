from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('volprofile', views.profile, name="profile"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('causes', views.causes, name="causes"),
    path('donate', views.donate, name="donate"),
    path('members', views.members, name="members"),
    path('volunteering', views.volunteering, name="volunteering"),
    path('base', views.base, name="base"),
    
    
    
    
    
]