from django.db import models
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

    u_id=models.CharField(max_length=12)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    branch=models.CharField(max_length=4,choices=branches)

    def __str__(self):
        return self.u_id

