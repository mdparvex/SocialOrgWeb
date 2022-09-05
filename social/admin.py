from django.contrib import admin
from .models import Profile, Study, Payment, Event

# Register your models here.
admin.site.register(Profile)
admin.site.register(Study)
admin.site.register(Payment)
admin.site.register(Event)
