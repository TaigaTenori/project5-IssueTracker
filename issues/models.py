from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class IssueModel(models.Model):
    """ A basic model for issues (posts) """
    
    name = models.CharField(max_length=144)
    body = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)