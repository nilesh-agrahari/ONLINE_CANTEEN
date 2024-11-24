from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from .forms import LoginForm
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

def login_check(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u_id = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(u_id=u_id)
                # Check if the entered password matches the hashed password
                if check_password(password, user.password):
                    request.session['user_id'] = user.u_id
                    return redirect('index2')
                else:
                    form.add_error(None, "Invalid User ID or Password")
            except User.DoesNotExist:
                form.add_error(None, "Invalid User ID or Password")
    else:
        form = LoginForm()

    return render(request, 'cankiet/login.html', {'form': form})   