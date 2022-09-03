from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from PIL import Image
# Create your models here.
User= get_user_model()
#first name, last name, email,pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=11)
    proffesion = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='image/')
    comment = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
    

class Study(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=50)
    institute_subject = models.CharField(max_length=10)
    institute_startDate = models.DateField()
    institute_endDate = models.DateField()

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_way = models.CharField(max_length=20)
    trxid = models.CharField(max_length=40)
    ammount = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)
    varified = models.BooleanField(default=False)

