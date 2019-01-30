from issues.models import IssueModel
from django.shortcuts import get_object_or_404

def latest_issues(request):
    issues = IssueModel.objects.order_by('created')[:10]
    return {'latest_issues': issues }
    
def cart_contents(request):
    cart = request.session.get('cart', {})
    

    total = len(cart) * 5
    product_count = len(cart)
    
    return {'cart': cart, 'cart_items': cart, 'total': total, 'product_count': product_count}