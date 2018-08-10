
# in mygame/web/links.py
 
from django.shortcuts import render
 
def testpage(request):
    return render(request, "test.html")
