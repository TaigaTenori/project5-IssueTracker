from django.shortcuts import render
from issues.models import IssueModel
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone

# Create your views here.

def get_data(request):
    month = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    total_issues = IssueModel.objects.filter(created__gte=month).count(),
    done_issues = IssueModel.objects.filter(created__gte=month).filter(progress__exact="Finished").count(),
    
    data = {
        
        'labels': ["Total issues"],
        'data': [total_issues, done_issues]
    }

    return JsonResponse(data, safe=False)
    
def stats(request):
    
    return render(request, 'stats.html')