from django import forms
from comments.models import Comment
from issues.models import IssueModel

from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    
    text = forms.CharField(label="Enter your comment (Max 1200 characters)", widget=forms.Textarea)


    class Meta:
        model = Comment
        fields = ['text']
    # add current user to author field