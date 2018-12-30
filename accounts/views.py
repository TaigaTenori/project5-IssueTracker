from django.shortcuts import render

# Create your views here.

def acccounts_index(request):
    return render(request, 'index.html')