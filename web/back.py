# in mygame/web/story.py

from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render

def testpage(request):
    return render(request, 'test.html')
