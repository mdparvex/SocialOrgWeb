from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User= get_user_model()
#first name, last name, email,pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=NULL)
    faceboo_link = models.CharField(max_length=50)
    attached_org_number = models.IntegerField(default=0)
    reffered_person_email = models.CharField(max_length=50)
    position = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    working_area = models.CharField(max_length=50)
    photo = models.ImageField(upload_to = 'image', default = 'default_img1.png')
    phone = models.IntegerField()
    father_name = models.CharField(max_length=30)
    father_phone = models.ImageField()
    mother_name = models.CharField(max_length=30)
    mother_phone = models.ImageField()
    gender = models.CharField(max_length=6)
    religin = models.CharField(max_length=10)
    technology_skill = models.CharField(max_length=40)
    cultural_skill = models.CharField(max_length=40)
    hobby = models.CharField(max_length=30)
    proffession = models.CharField(max_length=40)
    proffession_position = models.CharField(max_length=40)
    DOB = models.DateField()
    Natiolality = models.CharField(max_length=30)
    Identity_photo = models.ImageField(upload_to = 'identity', default = 'default_img2.png')
    present_address = models.CharField(max_length=100)
    permenent_address = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    intest_blood_donating = models.CharField(max_length=3)

class study(models.Model):
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
    varified = models.BooleanField(default=False)

