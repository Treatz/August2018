"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include

# default evennia patterns
from evennia.web.urls import urlpatterns

import story

from web import char

from web import test

from web import links

from web import test

from web import about

from web import fiction

from web import astrology
# eventual custom patterns

patterns = [
    url(r'^chargen/', include('web.chargen.urls')),
]
custom_patterns = [
    url(r'^character/', include('web.character.urls', namespace='character', app_name='character')),
    url(r'story', story.storypage, name='Story'),
    url(r'^ff/', include('web.ff.urls', namespace='ff', app_name='ff')),
    url(r'char', char.charpage, name='char'),
    url(r'links', links.linkspage, name='Links'),
    url(r'test', test.testpage, name='Test'),
    url(r'about', about.aboutpage, name='About'),
    url(r'fiction', fiction.fictionpage, name='Fiction'),
    url(r'astrology', astrology.astrologypage, name='Astrology'),
    ]

# this is required by Django.
urlpatterns = patterns + custom_patterns + urlpatterns
