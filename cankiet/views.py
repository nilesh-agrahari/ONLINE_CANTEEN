from django.shortcuts import render
from .models import User
def index2(request):
    user=User.objects.all()
    return render(request, 'cankiet/index2.html', {'user': user})

def login(request):
    user=User.objects.all()
    return render(request, 'cankiet/login.html', {'user': user})    
 
def orders(request):
    user=User.objects.all()
    return render(request, 'cankiet/orders.html', {'user': user} )  