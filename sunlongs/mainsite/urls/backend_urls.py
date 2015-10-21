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
    url(r'^login.html$', backend_views.admin_login, name='admin_login'),
    url(r'^logout.html$', backend_views.admin_logout, name='admin_logout'),
    url(r'^edit/logout.html$', backend_views.admin_logout, name='admin_logout'),
    url(r'^forget.html$', backend_views.forget_password, name='forget_password'),
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
    url( r'^images/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/images/' }
    ),
    url( r'^edit/font/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/fonts/' }
    ),
    url( r'^font/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/backend/fonts/' }
    ),
    url( r'^file/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/file/'}
    ),
    url( r'^edit/file/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/file/'}
    ),
    url( r'^edit/product/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': TEMPLATE_DIRS+'/../../media/product/'}
    ),
    url(r'^new_article$', backend_views.new_article, name='new_article'),
    url(r'^delete_article$', backend_views.delete_article, name='delete_article'),
    url(r'^edit_article$', backend_views.edit_article, name='edit_article'),
    url(r'^upload_file$', backend_views.upload_file, name='upload_file'),
    url(r'^ajax_upload_file$', backend_views.ajax_upload_file, name='ajax_upload_file'),
    url(r'^delete_file$', backend_views.delete_file, name='delete_file'),
    url(r'^edit_file$', backend_views.edit_file, name='edit_file'),
    
)
