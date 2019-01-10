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
from issues.views import issues_list, new_issue, issue_details

urlpatterns = [
    path('', accounts_index),
    path('admin/', admin.site.urls),
    path('accounts/', accounts_index, name='profile'), #display profile after logging in?
    path('accounts/profile/<request_username>', accounts_profile,  name='request_username'),
    path('accounts/logout', logout, name='logout'),
    path('accounts/login', login, name='login'),
    path('accounts/register', register, name='register'),
    path('issues/', issues_list, name='home'),
    path('issues/new/', new_issue, name='new_issue'),
    path('issues/<pk>', issue_details, name='issue_details'),
]
