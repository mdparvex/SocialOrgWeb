from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('volprofile', views.profile, name="profile"),
    path('donate', views.donate, name="donate"),
    path('volunteer', views.volunteer, name="volunteer"),
    path('base', views.base, name="base"),
    
    
    
    
    
]