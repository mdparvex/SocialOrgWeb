from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('volunteer', views.volunteer, name="volunteer"),
    path('base', views.base, name="base"),
    
    
    
]