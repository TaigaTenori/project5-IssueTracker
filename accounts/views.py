from django.shortcuts import render
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Create your views here.

def acccounts_index(request):
    return render(request, 'index.html')
    
def login(request):
    form = UserLoginForm(request.POST if request.POST else None)
    if request.method == "POST":
        if form.is_valid():
            # user will either be a User object or False
            user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
            if user:
                messages.success(request, "You have successfully logged in!")
                auth.login(user = user, request = request)
            else:
                #messages.error("The username or password is invalid")
                form.add_error(None, "The username or password is invalid")
        else:
            form.add_error(None, "There was an error with form input")
            
    return render(request, 'login.html', {"form": form })
    
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "You have been successfully logged out!")
    else:
        messages.success(request, "You are not logged in.")
    
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')