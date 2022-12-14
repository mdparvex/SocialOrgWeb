from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('join', views.join, name="join"),
    path('members', views.members, name="members"),
    path('member/<int:uid>', views.profile, name='profile'),
    path('history/<int:id>', views.history, name='history'),
    path('edit', views.editprofile, name='editprofile'),

    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('causes', views.causes, name="causes"),
    path('donate', views.donate, name="donate"),
    path('volunteering', views.volunteering, name="volunteering"),
    
    
]