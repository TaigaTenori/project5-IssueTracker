from django.db import models
from issues.models import IssueModel
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(IssueModel, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    
    text = models.TextField(blank=False, max_length=1200)
    
    
