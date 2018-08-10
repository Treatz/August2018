# Create your views here.
from django.shortcuts import render

def index(request):
    """The 'index' view."""
    return render(request, "ff//index.html")
