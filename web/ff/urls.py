# URL patterns for the help_system app

from django.conf.urls import url
from web.ff.views import index

urlpatterns = [
    url(r'^$', index, name="index")
]
