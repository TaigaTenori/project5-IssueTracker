from django.shortcuts import render
from django.contrib.auth.models import User
from issues.models import IssueModel
# Create your views here.

def issues_list(request):
    users = User.objects.all()
    
    #post = IssueModel(name=" Another Example topic", body=" And yet another example body text", author=users[0])
    #post.save()
    issues = IssueModel.objects.all()
    return render(request, 'issues.html', { 'users': users, 'issues':issues})