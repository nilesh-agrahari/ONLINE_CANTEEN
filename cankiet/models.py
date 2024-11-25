from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
# Create your models here.

class User(models.Model):
    branches=[
        ('Mca','MCA'),
        ('Bph','Btech Pharmacy'),
        ('Bcse','Btech CSE'),
        ('Bit','Btech IT'),
        ('Bece','Btech ECE'),
        ('Mba','MBA'),
    ]

    u_id=models.CharField(max_length=12,)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    branch=models.CharField(max_length=4,choices=branches)

    def save(self, *args, **kwargs):
        # Hash the password only if it is not already hashed
        if not self.password.startswith('pbkdf2_'):  # Check if password is already hashed
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.u_id

class Items(models.Model):
    i_no=models.CharField(max_length=12)
    item=models.CharField(max_length=20)
    i_image=models.ImageField(upload_to='images/')
    price=models.IntegerField()
    c_no=models.CharField(max_length=12)
    availability=models.CharField(max_length=1)
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.item

