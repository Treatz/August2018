
# in mygame/web/astrology.py
 
from django.shortcuts import render
 
def astrologypage(request):
    return render(request, "astrology.html")
