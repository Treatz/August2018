# file mygame/web/chargen/urls.py

from django.conf.urls import url
from web.chargen import views

urlpatterns = [
    # ex: /chargen/
    url(r'^$', views.index, name='index'),
    # ex: /chargen/5/
    url(r'^detail/$', views.detail, name='detail'),
    # ex: /chargen/create
    url(r'^create/$', views.creating, name='creating'),
]