from backend import views
from django.conf.urls import patterns, url
import os.path


TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/')


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^edit_home.html$', views.index, name='edit_home'),
    url(r'^edit_company.html$', views.index, name='edit_company'),
    url(r'^edit_news.html$', views.index, name='edit_news'),
    url(r'^edit_customer.html$', views.index, name='edit_customer'),
    url(r'^edit_contact.html$', views.index, name='edit_contact'),
    url(r'^gallery.html$', views.index, name='gallery'),
    url(r'^email.html$', views.index, name='email'),
    url(r'^setting.html$', views.index, name='setting'),
    url( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/js/' }
    ),
    url( r'^css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/css/' }
    ),
    url( r'^img/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/images/' }
    ),
    url( r'^font/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/fonts/' }
    )
)
