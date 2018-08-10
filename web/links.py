
# in mygame/web/links.py
 
from django.shortcuts import render
 
def linkspage(request):
    return render(request, "links.html")
