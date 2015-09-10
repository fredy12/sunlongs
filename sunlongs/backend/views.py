# -*- coding: utf-8 -*-
'''
Created on 2015-6-5

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''

from django.shortcuts import render
from backend.models import TextInfo, ImageInfo


# Create your views here.
def index(request):
    context = {
        'test_env_list': ''
    }
    return render(request, 'backend/index.html', context)

##  edit  ##

def edit_home(request):
    context = {}
    return render(request, 'backend/edit_home.html', context)

def edit_company(request):
    context = {}
    return render(request, 'backend/edit_company.html', context)

def edit_product(request):
    context = {}
    return render(request, 'backend/edit_product.html', context)

def edit_news(request):
    context = {}
    return render(request, 'backend/edit_news.html', context)

def edit_customer(request):
    context = {}
    return render(request, 'backend/edit_customer.html', context)

def edit_contact(request):
    context = {}
    return render(request, 'backend/edit_contact.html', context)

##  end of edit ##

##  gallery  ##

def gallery(request):
    all_images = ImageInfo.objects.all()
    all_texts = TextInfo.objects.all()
    
    
    
    context = {}
    return render(request, 'backend/gallery.html', context)

##  end of gallery  ##

def email(request):
    context = {}
    return render(request, 'backend/email.html', context)

def setting(request):
    context = {}
    return render(request, 'backend/setting', context)

