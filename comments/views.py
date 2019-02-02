from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from issues.models import IssueModel
from comments.forms import CommentForm

# Create your views here.

def add_comment(request, issue_id):
    print(request.user.id)
    if request.method == "POST":
        print("got hjim coach" + request.POST['text'])
        form = CommentForm(request.POST)
        if form.is_valid():
            tmp = form.save(commit = False)
            tmp.author = request.user
            tmp.issue = get_object_or_404(IssueModel, pk = issue_id)
            tmp.save()
            messages.success(request, "Your comment has been added.")
            #return redirect(reverse('home'))
    
    return redirect(reverse('home'))