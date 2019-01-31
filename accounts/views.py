from django.shortcuts import render, redirect
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from issues.models import IssueModel, UpvoteModel
from django.shortcuts import get_object_or_404

# Create your views here.

def accounts_index(request):
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
    form = UserRegistrationForm(request.POST if request.POST else None)
    if request.method == "POST":
        if form.is_valid():
            messages.success(request, "Registration successfull. You can now login with your name and password.")
            form.save()
            return redirect('login')
        else:
            form.add_error(None, 'Registration failed. Check the errors below.')
    
    return render(request, 'register.html', {'form': form})
    
def accounts_profile(request, request_username):
    messages.success(request, 'you have requested a profile of user: ' + request_username)

    user = get_object_or_404(User, username = request_username)
    
    issues = IssueModel.objects.filter(author = request_username)[:10]
    upvotes = UpvoteModel.objects.filter(user = get_object_or_404(User, username = request_username))
    return render(request, 'profile.html', { 'profile_user': user, 'issues': issues, 'upvotes': upvotes })