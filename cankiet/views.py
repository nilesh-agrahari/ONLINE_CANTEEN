from django.shortcuts import render

def index2(request):
    return render(request, 'cankiet/index2.html')

def login(request):
    return render(request, 'cankiet/login.html')    
 