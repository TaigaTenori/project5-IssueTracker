from django.shortcuts import render
from django.contrib import auth, messages

# Create your views here.

def acccounts_index(request):
    return render(request, 'index.html')
    
def login(request):
    return render(request, 'login.html')
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "You have been successfully logged out!")
    else:
        messages.success(request, "You are not logged in.")
    
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')