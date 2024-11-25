
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index2, name='index2'),
    path('login/',views.login, name='login'),
    path('orders/',views.orders, name='orders'),
    path('check/', views.login_check, name='check'),
    path('logout/', views.logout, name='logout'),
    path('canteens/', views.canteens, name='canteens'),
    path('cart/', views.cart, name='cart'),
    

]