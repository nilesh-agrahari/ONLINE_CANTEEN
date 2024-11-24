
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.login, name='login'),
    path('index2/',views.index2, name='index2'),
    path('orders/',views.orders, name='orders'),
    path('check/', views.login_check, name='check'),

]