from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import User,Items
def index2(request):
    user=User.objects.all()
    # Check if 'user_id' exists in the session
    if 'user' not in request.session:
        return redirect('login')  # Replace 'login' with the name of your login URL
    # If session exists, render the index page
    return render(request, 'cankiet/index2.html', {'user': user})

def login(request):
    user=User.objects.all()
    return render(request, 'cankiet/login.html', {'user': user})  

def logout(request):
    # Clear the session
    request.session.flush()  # Removes all session data
    return redirect('login')  # Redirect to the login page  
 
def orders(request):
    user=User.objects.all()
    food=Items.objects.all()
    return render(request, 'cankiet/orders.html', {'user': user,'food':food}) 

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
                    # Store all user attributes in the session
                    request.session['user'] = {
                    'user_id': user.u_id,
                    'name': user.name,
                    'phone': user.phone,
                    'dept': user.branch,
                    }
                    return redirect('index2')
                else:
                    form.add_error(None, "Invalid User ID or Password")
            except User.DoesNotExist:
                form.add_error(None, "Invalid User ID or Password")
    else:
        form = LoginForm()

    return render(request, 'cankiet/login.html', {'form': form})   