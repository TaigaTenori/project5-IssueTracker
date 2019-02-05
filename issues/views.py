from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from issues.models import IssueModel, UpvoteModel
from issues.forms import IssueCreationForm
from comments.forms import CommentForm
from comments.models import Comment
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
            return redirect(reverse('issue_details', args=[new_author.id]))
        else:
            form.add_error(None, "You have to be authenticated to post new issues.")
    else:
        form = IssueCreationForm(None)

    
    return render(request, 'new_issue.html', {'form': form })
    
def issue_details(request, pk):
    
    
    issue = IssueModel.objects.get(pk = pk)
    upvoted = True
    comments = Comment.objects.filter(issue = issue)
    form = CommentForm(None)
    if request.user.is_authenticated:
        upvoted = UpvoteModel.objects.filter(user = request.user, product = issue)
        
    return render(request, 'issue_details.html', {'issue': issue, 'upvoted': upvoted, 'comment_form': form, 'comments': comments})
    
@login_required()
def add_bug_upvote(request, issue_id):
    issue = IssueModel.objects.get(pk = issue_id)
    issue.upvotes += 1
    issue.save()
    upvote = UpvoteModel(product = issue , user = request.user)
    upvote.save()
    
    messages.add_message(request, messages.INFO, 'The issue has been upvoted successfully.')
    return redirect(reverse('issue_details', args=[issue.id]))