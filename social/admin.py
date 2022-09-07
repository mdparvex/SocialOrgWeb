from django.contrib import admin
from .models import Profile, Study, Donate, Event

# Register your models here.
admin.site.register(Profile)
admin.site.register(Study)
admin.site.register(Donate)
admin.site.register(Event)
