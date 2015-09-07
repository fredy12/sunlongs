from chinese import views
from django.conf.urls import patterns, url
import os.path


TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url( r'^(?P<path>.html)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/chinese/' }
    ),
    url( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/js/' }
    ),
    url( r'^css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/css/' }
    ),
    url( r'^images/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/images/' }
    ),
    url( r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/fonts/' }
    )
)
