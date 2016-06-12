# -*- coding: utf-8 -*-
'''
Created on 2015-9-23

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''
from mainsite.lib.utils import record_visit, reject_not_slongpump
from mainsite.models import ArticleInfo, FileInfo, CompanyInfo, ProductInfo, \
    ProductType, FileInfoForm, ArticleInfoForm, CompanyInfoForm, ProductInfoForm, \
    ProductTypeForm, NewsInfo, NewsInfoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import logging
import json
import os


logger = logging.getLogger(__name__)


def _get_common_info():
    logo_image = FileInfo.objects.filter(media_type='image', type='base', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = FileInfo.objects.filter(media_type='image', type='base', tag='rolling')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    return logo_image, rolling_images, company, product_types


@reject_not_slongpump
@record_visit
def index(request):
    logo_image, rolling_images, company, product_types = _get_common_info()

    product_divides = []
    for product_type in product_types:
        product_divides.append({'product_type': product_type, 'products': ProductInfo.objects.filter(lang='chinese', type__id=product_type.id)})
    all_news = NewsInfo.objects.filter(lang='chinese').order_by('-create_time')[0:5]
    return render(request, 'chinese/html/index.html', {'rolling_images': rolling_images, 'logo_image': logo_image,
                                                       'company': company,
                                                       'product_types': product_types, 'product_divides': product_divides,
                                                       'all_news': all_news})


@reject_not_slongpump
@record_visit
def company(request):
    logo_image, rolling_images, company, product_types = _get_common_info()
    return render(request, 'chinese/html/company.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})


@reject_not_slongpump
@record_visit
def culture(request):
    logo_image, rolling_images, company, product_types = _get_common_info()
    return render(request, 'chinese/html/culture.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})


@reject_not_slongpump
@record_visit
def application(request):
    logo_image, rolling_images, company, product_types = _get_common_info()
    return render(request, 'chinese/html/application.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})


@reject_not_slongpump
@record_visit
def certificate(request):
    logo_image, rolling_images, company, product_types = _get_common_info()
    certificate_images = FileInfo.objects.filter(media_type='image', type='base', tag='certificate')
    return render(request, 'chinese/html/certificate.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                             'product_types': product_types, 'certificate_images': certificate_images})


@reject_not_slongpump
@record_visit
def product(request):
    logo_image, rolling_images, company, product_types = _get_common_info()

    page_num = int(request.GET.get('page_num', 1))
    product_type_id = int(request.GET.get('type_id', -1))
    
    if product_type_id == -1:
        # means all product types
        products = ProductInfo.objects.filter(lang='chinese')[(page_num-1)*9:page_num*9]
        page_count = ProductInfo.objects.filter(lang='chinese').count() / 10 + 1
    else:
        products = ProductInfo.objects.filter(lang='chinese', type__id=product_type_id)[(page_num-1)*9:page_num*9]
        page_count = ProductInfo.objects.filter(lang='chinese', type__id=product_type_id).count() / 10 + 1
    
    return render(request, 'chinese/html/product.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types, 'products': products,
                                                         'select_product_type_id': product_type_id,
                                                         'page_count': xrange(1, page_count+1),
                                                         'now_page_num': page_num,
                                                         'max_page_num': page_count})


@reject_not_slongpump
@record_visit
def product_detail(request):
    logo_image, rolling_images, company, product_types = _get_common_info()
    
    product_id = request.GET.get('id', 1)
    product = ProductInfo.objects.filter(lang='chinese', id=product_id)
    if len(product) != 0:
        product = product[0]
    return render(request, 'chinese/html/product_detail.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                                'product_types': product_types, 'product': product})


@reject_not_slongpump
@record_visit
def news(request):
    logo_image, rolling_images, company, product_types = _get_common_info()
    
    page_num = int(request.GET.get('page_num', 1))
    all_news = NewsInfo.objects.filter(lang='chinese', status=1).order_by('-create_time')[(page_num-1)*9:page_num*9]
    page_count = NewsInfo.objects.filter(lang='chinese', status=1).count() / 10 + 1
    
    return render(request, 'chinese/html/news.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                      'product_types': product_types, 'all_news': all_news,
                                                      'page_count': xrange(1, page_count+1),
                                                      'now_page_num': page_num,
                                                      'max_page_num': page_count,
                                                      'now_date': datetime.now()})


@reject_not_slongpump
@record_visit
def news_detail(request):
    logo_image, rolling_images, company, product_types = _get_common_info()
    
    news_id = request.GET.get('id', 1)
    news = NewsInfo.objects.filter(lang='chinese', id=news_id, status=1)
    if len(news) != 0:
        news = news[0]
    return render(request, 'chinese/html/news_detail.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                             'product_types': product_types, 'news': news})


@reject_not_slongpump
@record_visit
def order(request):
    return render(request, 'chinese/html/order.html', {})


@reject_not_slongpump
@record_visit
def service(request):
    return render(request, 'chinese/html/service.html', {})


@reject_not_slongpump
@record_visit
def contact(request):
    logo_image, rolling_images, company, product_types = _get_common_info()
    return render(request, 'chinese/html/contact.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})


@reject_not_slongpump
@record_visit
def sitemap(request):
    return render(request, 'chinese/html/sitemap.html', {})
