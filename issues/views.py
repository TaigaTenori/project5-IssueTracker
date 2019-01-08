from django.shortcuts import render
from django.contrib.auth.models import User
from issues.models import IssueModel
from issues.forms import IssueCreationForm
# Create your views here.

def issues_list(request):
    users = User.objects.all()
    
    #post = IssueModel(name=" Hmmm", body=" Very much much better man", author=users[0])
    #post.save()
    issues = IssueModel.objects.all()
    return render(request, 'issues.html', { 'users': users, 'issues':issues})
    
def new_issue(request):
    
    if request.method == "POST":
        pass
    
    form = IssueCreationForm(None)
    
    return render(request, 'new_issue.html', {'form': form })
    