
# in mygame/web/links.py
 
from django.shortcuts import render
 
def aboutpage(request):
    return render(request, "about.html")
