from mainsite.views import default_views
from django.conf.urls import patterns, url
import os.path


TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), '../templates').replace('\\','/')


urlpatterns = patterns('',
    url(r'^$', default_views.index, name='index'),
)
