from issues.models import IssueModel


def latest_issues(request):
    issues = IssueModel.objects.all().order_by('created')[:10]
    return {'issues': issues }
    
