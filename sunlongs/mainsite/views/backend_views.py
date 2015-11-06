# -*- coding: utf-8 -*-
'''
Created on 2015-6-5

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mainsite.lib import file_lib
from mainsite.lib.utils import reject_not_slongpump
from mainsite.models import ArticleInfo, FileInfo, CompanyInfo, ProductInfo, VisitInfo, \
    ProductType, FileInfoForm, ArticleInfoForm, CompanyInfoForm, ProductInfoForm, \
    ProductTypeForm, NewsInfo, NewsInfoForm
from django.utils.timezone import now, timedelta
from django.core.mail import send_mail
from django.conf import settings

import json
import md5
import os
import random
import re
import uuid
import logging


logger = logging.getLogger(__name__)


@reject_not_slongpump
@login_required
def index(request):
    #create_time__gte=now().date() + timedelta(days=-1)
    visit_data = VisitInfo.objects.all().order_by('-create_time')
    if len(visit_data) != 0:
        yesterday_number = visit_data[0].number
        
        if len(visit_data) > 30:
            last_month_number = 0
            for n in visit_data[:30]:
                last_month_number += n.number
            if len(visit_data) > 365:
                last_year_number = 0
                for n in visit_data[:365]:
                    last_year_number += n.number
            else:
                last_year_number = 0
                for n in visit_data:
                    last_year_number += n.number
        
        else:
            last_month_number = 0
            last_year_number = 0
            for n in visit_data:
                last_month_number += n.number
                last_year_number += n.number
        
        if len(visit_data) > 10:
            last_10_days_list = visit_data[:10]
        else:
            last_10_days_list = visit_data
    else:
        yesterday_number = 0
        last_month_number = 0
        last_year_number = 0
        last_10_days_list = []
    return render(request, 'backend/html/index.html', {'account_name': settings.USER_NAME,
                                                       'yesterday_number': yesterday_number,
                                                       'last_month_number': last_month_number,
                                                       'last_year_number': last_year_number,
                                                       'last_10_days_list': last_10_days_list})

##  edit  ##

# edit base #

@csrf_exempt
@reject_not_slongpump
@login_required
def edit_base(request):
    rolling_images = FileInfo.objects.filter(type='基本信息', tag='首页滚动图片')
    logo_images = FileInfo.objects.filter(type='基本信息', tag='logo')
    certificate_images = FileInfo.objects.filter(type='基本信息', tag='资质认证')
    return render(request, 'backend/html/edit/base.html', {'account_name': settings.USER_NAME,
                                                           'rolling_images': rolling_images,
                                                           'logo_images': logo_images,
                                                           'certificate_images': certificate_images,
                                                           'type': '基本信息',
                                                           'rolling_tag': '首页滚动图片',
                                                           'logo_tag': 'logo',
                                                           'certificate_tag': '资质认证'})


# end edit base #

# edit company #

@csrf_exempt
@reject_not_slongpump
@login_required
def edit_company(request):
    if request.method == 'GET':
        lang = request.GET.get('lang', 'chinese')
        company_infos = CompanyInfo.objects.filter(lang=lang)
        page_data = {'account_name': settings.USER_NAME, 'company_info': {'lang': lang}}
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
@reject_not_slongpump
@login_required
def show_product(request):
    if request.method == 'GET':
        lang = request.GET.get('lang', 'chinese')
        product_types = ProductType.objects.filter(lang=lang)
        products = ProductInfo.objects.filter(lang=lang)
        return render(request, 'backend/html/edit/product.html', {'account_name': settings.USER_NAME,
                                                                  'lang': lang, 'products': products,
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
        return render(request, 'backend/html/edit/product.html', {'account_name': settings.USER_NAME,
                                                                  'lang': lang, 'products': products, 'product_types': product_types,
                                                                  'select_type_id': product_type_id})


@csrf_exempt
@reject_not_slongpump
@login_required
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
@reject_not_slongpump
@login_required
def delete_product(request):
    product_id = request.POST['id']
    product = ProductInfo.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect('product.html?lang='+request.POST['lang'])

##  end of edit product ##

## edit product type ##

@csrf_exempt
@reject_not_slongpump
@login_required
def product_type(request):
    chinese_product_types = ProductType.objects.filter(lang='chinese')
    english_product_types = ProductType.objects.filter(lang='english')
    return render(request, 'backend/html/edit/product_type.html', {'account_name': settings.USER_NAME,
                                                                   'chinese_product_types': chinese_product_types,
                                                                   'english_product_types': english_product_types})


@csrf_exempt
@reject_not_slongpump
@login_required
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
@reject_not_slongpump
@login_required
def delete_product_type(request):
    product_type_id = request.POST['id']
    # delete all the products before delete productType
    products = ProductInfo.objects.filter(type__id=product_type_id)
    for product in products:
        product.delete()
    product_type = ProductType.objects.get(id=product_type_id)
    product_type.delete()
    return HttpResponseRedirect('product_type.html')

## end of edit product type ##

## news ##

@reject_not_slongpump
@login_required
def news(request):
    # one page has 10 column
    cn_page_num = int(request.GET.get('cn_page_num', 1))
    en_page_num = int(request.GET.get('en_page_num', 1))
    chinese_news_info = NewsInfo.objects.filter(lang='chinese').order_by('-create_time')[(cn_page_num-1)*10:cn_page_num*10]
    english_news_info = NewsInfo.objects.filter(lang='english').order_by('-create_time')[(en_page_num-1)*10:en_page_num*10]
    chinese_page_count = NewsInfo.objects.filter(lang='chinese').count() / 11 + 1
    english_page_count = NewsInfo.objects.filter(lang='english').count() / 11 + 1
    return render(request, 'backend/html/news.html', {'account_name': settings.USER_NAME,
                                                      'chinese_news_info': chinese_news_info, 'chinese_page_count': xrange(1, chinese_page_count+1),
                                                      'english_news_info': english_news_info, 'english_page_count': xrange(1, english_page_count+1),
                                                      'cn_page_num': cn_page_num, 'en_page_num': en_page_num})


@csrf_exempt
@reject_not_slongpump
@login_required
def set_news_status(request):
    lang = request.POST.get('lang', 'chinese')
    news_id = request.POST['id']
    status = int(request.POST.get('status', False))
    NewsInfo.objects.filter(lang=lang, id=news_id).update(status=status)
    return HttpResponse("OK")


@csrf_exempt
@reject_not_slongpump
@login_required
def delete_news(request):
    news_id = request.POST['id']
    news = NewsInfo.objects.get(id=news_id)
    news.delete()
    return HttpResponseRedirect('news.html')


@csrf_exempt
@reject_not_slongpump
@login_required
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

@reject_not_slongpump
@login_required
def gallery(request):
    articles = ArticleInfo.objects.all().order_by('-create_time')
    images = FileInfo.objects.filter(media_type='image').order_by('-create_time')
    files = FileInfo.objects.filter(media_type='file').order_by('-create_time')
    return render(request, 'backend/html/gallery.html', {'account_name': settings.USER_NAME, 'articles': articles, 'images': images,
                                                         'files': files})


@csrf_exempt
@reject_not_slongpump
@login_required
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
@reject_not_slongpump
@login_required
def delete_article(request):
    article_id = request.POST['article_id']
    article = ArticleInfo.objects.get(id=article_id)
    article.delete()
    return HttpResponseRedirect('gallery.html')


@csrf_exempt
@reject_not_slongpump
@login_required
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
@reject_not_slongpump
@login_required
def upload_file(request):
    request.POST['display_name'] = request.FILES['file_info'].name
    file_lib.upload_file(request)
    redirect = request.POST.get('redirect', 'gallery.html')
    return HttpResponseRedirect(redirect)


@csrf_exempt
@reject_not_slongpump
@login_required
def ajax_upload_file(request):
    request.POST['display_name'] = request.FILES['file_info'].name
    if request.GET.has_key('dir'):
        request.POST['media_type'] = request.GET['dir']
    upload_file_obj = file_lib.upload_file(request)
    if upload_file_obj == None:
        response_data = {'error': 1, 'message': '上传文件失败'}
    else:
        # upload successfully
        response_data = {'error': 0, 'url': '/'.join(request.build_absolute_uri().split('/')[:-1]) + '/' + upload_file_obj.file_info.url}
    return HttpResponse(json.dumps(response_data))


@csrf_exempt
@reject_not_slongpump
@login_required
def delete_file(request):
    file_lib.delete_file(request)
    redirect = request.POST.get('redirect', 'gallery.html')
    return HttpResponseRedirect(redirect)


@csrf_exempt
@reject_not_slongpump
@login_required
def edit_file(request):
    file_lib.edit_file(request)
    redirect = request.POST.get('redirect', 'gallery.html')
    return HttpResponseRedirect(redirect)


##  end of gallery  ##

@reject_not_slongpump
@login_required
def email(request):
    context = {'account_name': settings.USER_NAME}
    return render(request, 'backend/html/email.html', context)


@reject_not_slongpump
@login_required
def setting(request):
    context = {'account_name': settings.USER_NAME}
    return render(request, 'backend/html/setting.html', context)


@csrf_exempt
@reject_not_slongpump
def admin_login(request):
    if request.method == 'GET':
        return render(request, 'backend/html/login.html', {})
    else:
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.GET.get('next')
        user = authenticate(username=username, password=password)
        if user != None:
            if user.is_active:
                login(request, user)
                if next_url == None:
                    return HttpResponseRedirect('/admin/index.html')
                else:
                    return HttpResponseRedirect(next_url)
            else:
                return render(request, 'backend/html/login.html', {'error_msg': '登录失败，账号或密码不正确。'})   #需要设置错误提示，无效账户
        else:
            return render(request, 'backend/html/login.html', {'error_msg': '登录失败，账号或密码不正确'})   #设置登录失败


@reject_not_slongpump
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect('/admin/login.html')


def generate_password():
    return str(uuid.uuid4())[-8:-4].upper() + random.choice('@#$!*abcdefghijklmnpqABCDEFGHIJKLMNPQ') + random.choice('@#$!*') + str(uuid.uuid4())[-4:].lower()+ random.choice('@#$!*')


def send_email(password):
    try:
        send_mail('重置密码信息', '重置账号为：%s，密码为：%s' % (settings.USER_NAME, password), settings.EMAIL_FROM_USER, [settings.EMAIL_TO_USER], fail_silently=False)
    except Exception, e:
        # log here
        print str(e)
        return False
    return True


@csrf_exempt
@reject_not_slongpump
def forget_password(request):
    if request.method == 'GET':
        return render(request, 'backend/html/forget.html', {})
    else:
        reset_password = request.POST['reset_password']
        if reset_password != settings.RESET_PASSWORD_MD5:
            return render(request, 'backend/html/forget.html', {'error_msg': '重置失败，口令不正确'})

        user = User.objects.filter(username__exact=settings.USER_NAME)
        if len(user) == 0:
            ### means need create user
            logger.debug('User not exist, start create user...')
            password = generate_password()
            if send_email(password):
                User.objects.create_user(settings.USER_NAME, settings.USER_EMAIL, password)
            else:
                return render(request, 'backend/html/forget.html', {'error_msg': '重置失败，重置邮件发送失败'})
        else:
            logger.debug('User exist, reset user password...')
            password = generate_password()
            if send_email(password):
                u = User.objects.get(username__exact=settings.USER_NAME)
                u.set_password(password)
                u.save()
            else:
                return render(request, 'backend/html/forget.html', {'error_msg': '重置失败，重置邮件发送失败'})

        return HttpResponseRedirect('login.html')
