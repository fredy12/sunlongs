# -*- coding: utf-8 -*-
'''
Created on 2015-9-23

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''
from mainsite.lib import image_lib
from mainsite.models import ArticleInfo, ImageInfo, CompanyInfo, ProductInfo, \
    ProductType, ImageInfoForm, ArticleInfoForm, CompanyInfoForm, ProductInfoForm, \
    ProductTypeForm, NewsInfo, NewsInfoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import os


# Create your views here.
def index(request):
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    product_divides = []
    for product_type in product_types:
        product_divides.append({'product_type': product_type, 'products': ProductInfo.objects.filter(lang='chinese', type__id=product_type.id)})
    all_news = NewsInfo.objects.filter(lang='chinese').order_by('-create_time')[0:5]
    return render(request, 'chinese/html/index.html', {'rolling_images': rolling_images, 'logo_image': logo_image,
                                                       'company': company,
                                                       'product_types': product_types, 'product_divides': product_divides,
                                                       'all_news': all_news})


def company(request):
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    return render(request, 'chinese/html/company.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})


def culture(request):
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    return render(request, 'chinese/html/culture.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})


def application(request):
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    return render(request, 'chinese/html/application.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})


def certificate(request):
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    return render(request, 'chinese/html/certificate.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})


def product(request):
    page_num = int(request.GET.get('page_num', 1))
    product_type_id = int(request.GET.get('type_id', -1))
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
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


def product_detail(request):
    product_id = request.GET.get('id', 1)
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    product = ProductInfo.objects.filter(lang='chinese', id=product_id)
    if len(product) != 0:
        product = product[0]
    return render(request, 'chinese/html/product_detail.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                                'product_types': product_types, 'product': product})


def news(request):
    page_num = int(request.GET.get('page_num', 1))
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    all_news = NewsInfo.objects.filter(lang='chinese', status=1).order_by('-create_time')[(page_num-1)*9:page_num*9]
    page_count = NewsInfo.objects.filter(lang='chinese', status=1).count() / 10 + 1
    
    return render(request, 'chinese/html/news.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                      'product_types': product_types, 'all_news': all_news,
                                                      'page_count': xrange(1, page_count+1),
                                                      'now_page_num': page_num,
                                                      'max_page_num': page_count,
                                                      'now_date': datetime.now()})


def news_detail(request):
    news_id = request.GET.get('id', 1)
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    news = NewsInfo.objects.filter(lang='chinese', id=news_id, status=1)
    if len(news) != 0:
        news = news[0]
    return render(request, 'chinese/html/news_detail.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                             'product_types': product_types, 'news': news})


def order(request):
    return render(request, 'chinese/html/order.html', {})


def service(request):
    return render(request, 'chinese/html/service.html', {})


def contact(request):
    logo_image = ImageInfo.objects.filter(type='基本信息', tag='logo')
    if len(logo_image) != 0:
        logo_image = logo_image[0]
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    company = CompanyInfo.objects.filter(lang='chinese')
    if len(company) != 0:
        company = company[0]
    product_types = ProductType.objects.filter(lang='chinese')
    return render(request, 'chinese/html/contact.html', {'rolling_images': rolling_images, 'logo_image': logo_image, 'company': company,
                                                         'product_types': product_types})
