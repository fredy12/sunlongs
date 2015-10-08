from mainsite.views import backend_views
from django.conf.urls import patterns, url
import os.path


TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), '../templates').replace('\\','/')


urlpatterns = patterns('',
    url(r'^$', backend_views.index, name='index'),
    url(r'^index.html$', backend_views.index, name='index'),
    url(r'^edit/base.html$', backend_views.edit_base, name='edit_base'),
    url(r'^edit/company.html$', backend_views.edit_company, name='edit_company'),
    url(r'^edit/product.html$', backend_views.show_product, name='show_product'),
    url(r'^edit/edit_product$', backend_views.edit_product, name='edit_product'),
    url(r'^edit/delete_product$', backend_views.delete_product, name='delete_product'),
    url(r'^edit/product_type.html$', backend_views.product_type, name='product_type'),
    url(r'^edit/edit_product_type$', backend_views.edit_product_type, name='edit_product_type'),
    url(r'^edit/delete_product_type$', backend_views.delete_product_type, name='delete_product_type'),
    url(r'^gallery.html$', backend_views.gallery, name='gallery'),
    url(r'^news.html$', backend_views.news, name='news'),
    url(r'^edit_news$', backend_views.edit_news, name='edit_news'),
    url(r'^delete_news$', backend_views.delete_news, name='delete_news'),
    url(r'^set_news_status$', backend_views.set_news_status, name='set_news_status'),
    url(r'^email.html$', backend_views.email, name='email'),
    url(r'^setting.html$', backend_views.setting, name='setting'),
    url( r'^edit/js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/js/' }
    ),
    url( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/js/' }
    ),
    url( r'^edit/css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/css/' }
    ),
    url( r'^css/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/css/' }
    ),
    url( r'^edit/img/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/images/' }
    ),
    url( r'^img/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/images/' }
    ),
    url( r'^edit/font/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/fonts/' }
    ),
    url( r'^font/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/fonts/' }
    ),
    url( r'^pic/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/pic/'}
    ),
    url( r'^edit/pic/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/pic/'}
    ),
    url( r'^edit/product/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/product/'}
    ),
    url(r'^new_article$', backend_views.new_article, name='new_article'),
    url(r'^delete_article$', backend_views.delete_article, name='delete_article'),
    url(r'^edit_article$', backend_views.edit_article, name='edit_article'),
    url(r'^upload_image$', backend_views.upload_image, name='upload_image'),
    url(r'^delete_image$', backend_views.delete_image, name='delete_image'),
    url(r'^edit_image$', backend_views.edit_image, name='edit_image'),
    
)
