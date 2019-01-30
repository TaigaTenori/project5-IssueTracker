from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class IssueModel(models.Model):
    """ A basic model for issues (posts) """
    
    name = models.CharField(max_length=144)
    body = models.TextField(blank=False)
    author = models.CharField(max_length=50, editable=False) # can also use : exclude = ['author']
    price = 5
    
    created = models.DateTimeField(auto_now=True)
    type_choices = {
        ('BUG', 'Bug Report'),
        ('FEATURE', 'Feature Request') 
    }
    type = models.CharField(
        max_length = 15,
        choices = type_choices,
        default = 'BUG'
    )
    upvotes = models.IntegerField(default=0)
    

    progress_choices = (
        ('NOT_STARTED', 'Inactive'),
        ('IN_PROGRESS', 'In progress'),
        ('FINISHED', 'Done')
    )
    progress = models.CharField(
        max_length = 12,
        default = 'NOT_STARTED'
    )