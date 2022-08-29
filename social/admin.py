from django.contrib import admin
from .models import Profile, Study, Payment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Study)
admin.site.register(Payment)
