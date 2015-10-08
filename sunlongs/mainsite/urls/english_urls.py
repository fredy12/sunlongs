from mainsite.views import english_views
from django.conf.urls import patterns, url
import os.path


TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), '../templates').replace('\\','/')


urlpatterns = patterns('',
    url(r'^$', english_views.index, name='index'),
    url(r'^index.html$', english_views.index, name='index'),
    url(r'^company.html$', english_views.company, name='company'),
    url(r'^culture.html$', english_views.culture, name='culture'),
    url(r'^application.html$', english_views.application, name='application'),
    url(r'^certificate.html$', english_views.certificate, name='certificate'),
    url(r'^product.html$', english_views.product, name='product'),
    url(r'^product_detail.html$', english_views.product_detail, name='product_detail'),
    url(r'^news.html$', english_views.news, name='news'),
    url(r'^news_detail.html$', english_views.news_detail, name='news_detail'),
    url(r'^order.html$', english_views.order, name='order'),
    url(r'^service.html$', english_views.service, name='service'),
    url(r'^contact.html$', english_views.contact, name='contact'),
    url( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/english/js/' }
    ),
    url( r'^css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/english/css/' }
    ),
    url( r'^images/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/english/images/' }
    ),
    url( r'^font/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/english/fonts/' }
    ),
    url( r'^pic/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/pic/'}
    ),
    url( r'^product/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/product/'}
    ),
    
)
