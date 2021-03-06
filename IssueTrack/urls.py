"""IssueTrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import accounts_index, logout, login, register, accounts_profile
from issues.views import issues_list, new_issue, issue_details, add_bug_upvote, hot_issues
from cart.views import add_upvote, view_cart, cart_remove
from checkout.views import checkout
from comments.views import add_comment
from stats.views import get_data, stats


urlpatterns = [
    path('', accounts_index),
    path('admin/', admin.site.urls),
    path('accounts/profile/<request_username>', accounts_profile,  name='profile'),
    path('accounts/logout', logout, name='logout'),
    path('accounts/login/', login, name='login'),
    path('accounts/register', register, name='register'),
    path('issues/', issues_list, name='home'),
    path('issues/hot', hot_issues, name='hot_issues'),
    path('issues/new/', new_issue, name='new_issue'),
    path('issues/<pk>', issue_details, name='issue_details'),
    path('issues/add_bug_upvote/<issue_id>', add_bug_upvote, name='add_bug_upvote'),
    path('cart/add_upvote/<issue_id>/<issue_name>/<issue_price>', add_upvote, name='add_upvote'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/remove/<issue_id>', cart_remove, name='cart_remove'),
    path('checkout/', checkout, name = 'checkout'),
    path('comments/add_comment/<issue_id>', add_comment, name = 'add_comment'),
    path('api/data/<var>', get_data, name= 'api-data'),
    path('stats/', stats, name='stats')
]
