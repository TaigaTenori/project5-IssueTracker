from django.shortcuts import render, redirect, reverse
from issues.models import IssueModel
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.safestring import mark_safe

# Create your views here.

def add_upvote(request, issue_id, issue_name):
    cart = request.session.get('cart', {})
    
    if issue_id in cart:
        messages.add_message(request, messages.ERROR, "This upvote is already in your basket.")
        return redirect(reverse('view_cart'))
    
    cart[issue_id] = issue_name
    
    request.session['cart'] = cart
    
    messages.add_message(request, messages.INFO, mark_safe('This upvote (<a href="' + reverse('issue_details', args=[issue_id]) +'">go to issue</a>) has been added to your basket.'))
    
    return redirect(reverse('home'))
    
def view_cart(request):
    cart = request.session.get('cart', {})
    
    # store issue names that the user wants to upvote by paying

    """   
    for issue_id, quantity in cart.items():
        issue = get_object_or_404(IssueModel, pk=issue_id)
        cart_issues.append(issue)
    """   
    return render(request, 'view_cart.html', { 'cart': cart })
    
def cart_remove(request, issue_id):
    cart = request.session.get('cart', {})

    del request.session['cart'][issue_id]
    
    request.session.modified = True
    
    messages.add_message(request, messages.INFO, 'The upvote has been removed from your cart.')
    
    return redirect(reverse('view_cart'))