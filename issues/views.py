from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from issues.models import IssueModel, UpvoteModel
from issues.forms import IssueCreationForm
# Create your views here.

def issues_list(request):
    users = User.objects.all()
    
    issues = IssueModel.objects.all()
    return render(request, 'issues.html', { 'users': users, 'issues':issues})
    
def new_issue(request):
    
    if request.method == "POST":
        form = IssueCreationForm(request.POST)
        if form.is_valid and request.user.is_authenticated:
            
            """
                Was not sure how to automatically fill the 'author' field with the logged in user
                so I do that manually here, until I find a better way to do it.
            """
            new_author = form.save(commit=False)
            new_author.author = request.user
            new_author.save()
            messages.success(request, "Your post has been added!")
            redirect('home')
        else:
            form.add_error(None, "You have to be authenticated to post new issues.")
    else:
        form = IssueCreationForm(None)

    
    return render(request, 'new_issue.html', {'form': form })
    
def issue_details(request, pk):
    
    
    issue = IssueModel.objects.get(pk=pk)
    upvoted = UpvoteModel.objects.filter(user = request.user, product = issue)
    return render(request, 'issue_details.html', {'issue': issue, 'upvoted': upvoted})