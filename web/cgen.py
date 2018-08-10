# in mygame/web/story.py

from django.template.loader import get_template
from django.http import HttpResponse

def cgenpage(request):
    template = get_template("cgen.html")
    html = template.render()
    return HttpResponse(html)
