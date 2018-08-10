from django.template.loader import get_template
from django.http import HttpResponse

def storypage(request):
    template = get_template("mobile.html")
    html = template.render()
    return HttpResponse(html)
