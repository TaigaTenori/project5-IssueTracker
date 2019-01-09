from django import forms
from issues.models import IssueModel
from django.contrib.auth.models import User
class IssueCreationForm(forms.ModelForm):
    
    name = forms.CharField(label="Write a short summary of the issue")
    body = forms.CharField(label="Describe the issue", widget=forms.Textarea)
    type = forms.ChoiceField(label="Select what kind of issue it is", choices = IssueModel.type_choices)


    
    class Meta:
        model = IssueModel
        fields = ['name', 'body', 'type']
    # add current user to author field
    
