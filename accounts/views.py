from django.shortcuts import render

# Create your views here.

def acccounts_index(request):
    return render(request, 'index.html')
    
def login(request):
    return render(request, 'login.html')
    
def logout(request):
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')