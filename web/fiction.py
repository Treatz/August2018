
# in mygame/web/links.py
 
from django.shortcuts import render
 
def fictionpage(request):
    return render(request, "fiction.html")
