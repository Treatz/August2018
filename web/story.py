# in mygame/web/story.py

from django.template.loader import get_template
from django.http import HttpResponse

def storypage(request):
    template = get_template("story.html")
    html = template.render()
    return HttpResponse(html)
