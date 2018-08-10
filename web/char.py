from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render

def charpage(request):
    return render(request, 'char.html')
