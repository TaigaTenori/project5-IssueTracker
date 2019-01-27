from issues.models import IssueModel
from django.shortcuts import get_object_or_404

def latest_issues(request):
    issues = IssueModel.objects.order_by('created')[:10]
    return {'latest_issues': issues }
    
def cart_contents(request):
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0   
    
    for id, quantity in cart.items():
        if not quantity:
            quantity = 0
        issue = get_object_or_404(IssueModel, pk=id)
        total += quantity * 5
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': issue})
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}