from mainsite.views import chinese_views
from django.conf.urls import patterns, url
import os.path


TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), '../templates').replace('\\','/')


urlpatterns = patterns('',
    url(r'^$', chinese_views.index, name='index'),
    url(r'^index.html$', chinese_views.index, name='index'),
    url(r'^company.html$', chinese_views.company, name='company'),
    url(r'^culture.html$', chinese_views.culture, name='culture'),
    url(r'^application.html$', chinese_views.application, name='application'),
    url(r'^certificate.html$', chinese_views.certificate, name='certificate'),
    url(r'^product.html$', chinese_views.product, name='product'),
    url(r'^product_detail.html$', chinese_views.product_detail, name='product_detail'),
    url(r'^news.html$', chinese_views.news, name='news'),
    url(r'^news_detail.html$', chinese_views.news_detail, name='news_detail'),
    url(r'^order.html$', chinese_views.order, name='order'),
    url(r'^service.html$', chinese_views.service, name='service'),
    url(r'^contact.html$', chinese_views.contact, name='contact'),
    url( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/chinese/js/' }
    ),
    url( r'^css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/chinese/css/' }
    ),
    url( r'^images/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/chinese/images/' }
    ),
    url( r'^font/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/chinese/fonts/' }
    ),
    url( r'^file/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/file/'}
    ),
    url( r'^product/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/product/'}
    ),
    
)
