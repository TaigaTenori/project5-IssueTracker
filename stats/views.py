from django.shortcuts import render
from issues.models import IssueModel
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def get_data(request, var):
    time_period = timezone.now().date() - timedelta(days=7)
    if var == "month":
        time_period = timezone.now().date() - timedelta(days=30)
    total_issues = IssueModel.objects.filter(created__gte=time_period).count(),
    done_issues = IssueModel.objects.filter(created__gte=time_period).filter(progress__exact="Finished").count(),
    working_issues = IssueModel.objects.filter(created__gte=time_period).filter(progress__exact="in progress").count(),
    
    data = {
        
        'labels': ["Total issues"],
        'data': [total_issues, done_issues, working_issues]
    }

    return JsonResponse(data, safe=False)
    
def stats(request):
    
    return render(request, 'stats.html')