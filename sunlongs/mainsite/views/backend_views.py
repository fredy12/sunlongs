# -*- coding: utf-8 -*-
'''
Created on 2015-6-5

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''

from mainsite.lib import image_lib
from mainsite.models import ArticleInfo, ImageInfo, CompanyInfo, ProductInfo, \
    ProductType, ImageInfoForm, ArticleInfoForm, CompanyInfoForm, ProductInfoForm, \
    ProductTypeForm, NewsInfo, NewsInfoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import re
import os


# Create your views here.
def index(request):
    context = {
        'test_env_list': ''
    }
    return render(request, 'backend/html/index.html', context)

##  edit  ##

# edit base #

@csrf_exempt
def edit_base(request):
    rolling_images = ImageInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    logo_images = ImageInfo.objects.filter(type='基本信息', tag='logo')
    return render(request, 'backend/html/edit/base.html', {'rolling_images': rolling_images,
                                                           'logo_images': logo_images,
                                                           'type': '基本信息',
                                                           'rolling_tag': '首页滚动图片',
                                                           'logo_tag': 'logo'})


# end edit base #

# edit company #

@csrf_exempt
def edit_company(request):
    if request.method == 'GET':
        lang = request.GET.get('lang', 'chinese')
        company_infos = CompanyInfo.objects.filter(lang=lang)
        page_data = {'company_info': {'lang': lang}}
        if len(company_infos) != 0:
            page_data['company_info'] = company_infos[0]
        return render(request, 'backend/html/edit/company.html', page_data)
    else:
        language = request.POST['lang']
        companys = CompanyInfo.objects.filter(lang=language)
        if len(companys) == 0:
            # means add company
            form = CompanyInfoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        else:
            # means update company
            company = CompanyInfo.objects.get(lang=language)
            form = CompanyInfoForm(request.POST, request.FILES, instance=company)
            if form.is_valid():
                form.save()
        return HttpResponseRedirect('company.html?lang='+request.POST['lang'])

# end edit company #

# edit product #

@csrf_exempt
def show_product(request):
    if request.method == 'GET':
        lang = request.GET.get('lang', 'chinese')
        product_types = ProductType.objects.filter(lang=lang)
        products = ProductInfo.objects.filter(lang=lang)
        return render(request, 'backend/html/edit/product.html', {'lang': lang, 'products': products,
                                                                  'product_types': product_types})
    else:
        lang = request.POST.get('lang', 'chinese')
        product_type_id = int(request.POST.get('type', -1))
        if product_type_id == -1:
            # means all types
            products = ProductInfo.objects.filter(lang=lang)
        else:
            products = ProductInfo.objects.filter(lang=lang, type__id=product_type_id)
        product_types = ProductType.objects.filter(lang=lang)
        return render(request, 'backend/html/edit/product.html', {'lang': lang, 'products': products, 'product_types': product_types,
                                                                  'select_type_id': product_type_id})


@csrf_exempt
def edit_product(request):
    product_id = request.POST.get('id')
    if product_id == None or product_id == '':
        # new product
        form = ProductInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        # means update product
        product = ProductInfo.objects.get(id=product_id)
        # for delete the old picture before update product pic
        old_pic_path = ''
        if product.pic != '':
            # when input pic is not null, we will not delete the old one.
            if request.POST.get('pic') == None or request.POST.get('pic') == '':
                old_pic_path = ''
            else:
                old_pic_path = product.pic.path
        form = ProductInfoForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save_with_delete_old_pic(old_pic_path)
    return HttpResponseRedirect('product.html?lang='+request.POST['lang'])


@csrf_exempt
def delete_product(request):
    product_id = request.POST['id']
    product = ProductInfo.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect('product.html?lang='+request.POST['lang'])

##  end of edit product ##

## edit product type ##

@csrf_exempt
def product_type(request):
    chinese_product_types = ProductType.objects.filter(lang='chinese')
    english_product_types = ProductType.objects.filter(lang='english')
    return render(request, 'backend/html/edit/product_type.html', {'chinese_product_types': chinese_product_types,
                                                                   'english_product_types': english_product_types})


@csrf_exempt
def edit_product_type(request):
    product_type_id = request.POST.get('id')
    if product_type_id == None or product_type_id == '':
        # new product type
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        # update news
        product_type = ProductType.objects.get(id=product_type_id)
        form = ProductTypeForm(request.POST, instance=product_type)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('product_type.html')


@csrf_exempt
def delete_product_type(request):
    product_type_id = request.POST['id']
    product_type = ProductType.objects.get(id=product_type_id)
    product_type.delete()
    return HttpResponseRedirect('product_type.html')

## end of edit product type ##

## news ##

def news(request):
    # one page has 10 column
    cn_page_num = int(request.GET.get('cn_page_num', 1))
    en_page_num = int(request.GET.get('en_page_num', 1))
    chinese_news_info = NewsInfo.objects.filter(lang='chinese').order_by('-create_time')[(cn_page_num-1)*10:cn_page_num*10]
    english_news_info = NewsInfo.objects.filter(lang='english').order_by('-create_time')[(en_page_num-1)*10:en_page_num*10]
    chinese_page_count = NewsInfo.objects.filter(lang='chinese').count() / 11 + 1
    english_page_count = NewsInfo.objects.filter(lang='english').count() / 11 + 1
    return render(request, 'backend/html/news.html', {'chinese_news_info': chinese_news_info, 'chinese_page_count': xrange(1, chinese_page_count+1),
                                                 'english_news_info': english_news_info, 'english_page_count': xrange(1, english_page_count+1),
                                                 'cn_page_num': cn_page_num, 'en_page_num': en_page_num})


@csrf_exempt
def set_news_status(request):
    lang = request.POST.get('lang', 'chinese')
    news_id = request.POST['id']
    status = int(request.POST.get('status', False))
    NewsInfo.objects.filter(lang=lang, id=news_id).update(status=status)
    return HttpResponse({'status', 'OK'})


@csrf_exempt
def delete_news(request):
    news_id = request.POST['id']
    news = NewsInfo.objects.get(id=news_id)
    news.delete()
    return HttpResponseRedirect('news.html')


@csrf_exempt
def edit_news(request):
    news_id = request.POST.get('id')
    if news_id == None or news_id == '':
        # new news
        # add intro
        # ignore content html <>
        request.POST['intro'] = '  '.join(re.split('<[^>]+>', request.POST['content']))[0:60] + '...'
        form = NewsInfoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        # update news
        news = NewsInfo.objects.get(id=news_id)
        # add intro
        request.POST['intro'] = '  '.join(re.split('<[^>]+>', request.POST['content'])).replace('\r', '').replace('\n', '').replace('\t', '')[0:60] + '...'
        form = NewsInfoForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect('news.html')

## end of news ##

##  gallery  ##

def gallery(request):
    articles = ArticleInfo.objects.all().order_by('-create_time')
    images = ImageInfo.objects.all().order_by('-create_time')
    return render(request, 'backend/html/gallery.html', {'articles': articles, 'images': images})


@csrf_exempt
def new_article(request):
    # means add ariticle
    # add intro
    request.POST['intro'] = request.POST['content'][0:60] + '......'
    form = ArticleInfoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('gallery.html')
    return gallery(request)


@csrf_exempt
def delete_article(request):
    article_id = request.POST['article_id']
    article = ArticleInfo.objects.get(id=article_id)
    article.delete()
    return HttpResponseRedirect('gallery.html')


@csrf_exempt
def edit_article(request):
    article_id = request.POST['article_id']
    # means update article
    article = ArticleInfo.objects.get(id=article_id)
    # add intro
    request.POST['intro'] = request.POST['content'][0:60] + '......'
    form = ArticleInfoForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('gallery.html')
    return gallery(request)


@csrf_exempt
def upload_image(request):
    image_lib.upload_image(request)
    redirect = request.POST.get('redirect', 'gallery.html')
    return HttpResponseRedirect(redirect)


@csrf_exempt
def delete_image(request):
    image_lib.delete_image(request)
    redirect = request.POST.get('redirect', 'gallery.html')
    return HttpResponseRedirect(redirect)


@csrf_exempt
def edit_image(request):
    image_lib.edit_image(request)
    redirect = request.POST.get('redirect', 'gallery.html')
    return HttpResponseRedirect(redirect)


##  end of gallery  ##

def email(request):
    context = {}
    return render(request, 'backend/html/email.html', context)

def setting(request):
    context = {}
    return render(request, 'backend/html/setting', context)

