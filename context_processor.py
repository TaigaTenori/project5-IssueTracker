from issues.models import IssueModel


def latest_issues(request):
    issues = IssueModel.objects.order_by('created')[:10]
    return {'latest_issues': issues }
    
