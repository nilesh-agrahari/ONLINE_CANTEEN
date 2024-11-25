from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now
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

    u_id=models.CharField(max_length=12,primary_key=True)
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
    i_no=models.CharField(max_length=12,primary_key=True)
    item=models.CharField(max_length=20)
    i_image=models.ImageField(upload_to='images/')
    price=models.IntegerField()
    c_no=models.CharField(max_length=12)
    availability=models.CharField(max_length=1)
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.item

class Canteen(models.Model):
    c_no=models.CharField(max_length=2,primary_key=True,)
    c_name=models.CharField(max_length=20)

    def __str__(self):
        return self.c_name
    
class Order(models.Model):
    o_no = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    o_date = models.DateTimeField(default=now)  # Automatically stores the current date and time
    i_no = models.ForeignKey('Item', on_delete=models.CASCADE)  # Foreign key to Item table
    u_id = models.ForeignKey('User', on_delete=models.CASCADE)  # Foreign key to User table
    c_no = models.ForeignKey('Canteen', on_delete=models.CASCADE)  # Foreign key to Canteen table

    def __str__(self):
        return f"Order {self.o_no} - {self.o_date.strftime('%Y-%m-%d %H:%M:%S')}"