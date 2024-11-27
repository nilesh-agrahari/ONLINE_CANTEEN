from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login
from django.utils.timezone import now
import uuid
from .forms import LoginForm
from .models import User,Items,Canteen,Order
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

def canteens(request,):
    canteen=Canteen.objects.all()
    return render(request, 'cankiet/canteens.html', {'canteen':canteen,})

def menu(request,c_no):
     # Fetch the selected canteen
    canteen = get_object_or_404(Canteen, c_no=c_no)
    # Fetch items for the selected canteen
    items = Items.objects.filter(c_no=canteen.c_no)
    # Pass data to the template
    return render(request, 'cankiet/menu.html', {'canteen': canteen, 'items': items})

def food(request,c_no):
     # Fetch the selected canteen
    canteen = get_object_or_404(Canteen, c_no=c_no)
    # Fetch items for the selected canteen
    items = Items.objects.filter(c_no=canteen.c_no)
    # Pass data to the template
    return render(request, 'cankiet/orderfoodpage.html', {'canteen': canteen, 'items': items})


def cart(request,c_no):
    
    canteen = get_object_or_404(Canteen, c_no=c_no)
    if request.method == 'POST':
        item_id = request.POST.get('i_no')
        quantity = int(request.POST.get('quantity', 1))
        # Fetch the item
        items = get_object_or_404(Items,i_no=item_id)
        total_amount=quantity*items.price

    return render(request, 'cankiet/cart.html',{'canteen': canteen, 'items': items,'quantity':quantity,'total':total_amount})

def confirmation(request,c_no):
    canteen = get_object_or_404(Canteen, c_no=c_no)
    if request.method == 'POST':
        # Generate Order Number
        timestamp = now().strftime('%Y%m%d%H%M%S')
        o_no = f"ORD{timestamp}{str(uuid.uuid4().int)[:6]}"
        date=now()
        item_id = request.POST.get('i_no')
        quantity = int(request.POST.get('quantity', 1))
        total=int(request.POST.get('total'))
        # Fetch the item
        items = get_object_or_404(Items,i_no=item_id)
        Order.objects.create(
                o_no=o_no,
                o_date=now(),
                # u_id=user.u_id,  # Reference to logged-in user
                c_no=canteen,  # Reference to the related canteen
                item=items,
                quantity=quantity,
                total_amount=total,
            )
        order=get_object_or_404(Order,o_no=o_no)
    return render(request, 'cankiet/confirmation.html',{'o_no':o_no,'total_amount':total,'date':date,'order':order})

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
                    'u_id': user.u_id,
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