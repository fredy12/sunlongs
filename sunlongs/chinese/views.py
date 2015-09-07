# -*- coding: utf-8 -*-
'''
Created on 2015-6-5

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''

from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'test_env_list': ''
    }
    return render(request, 'chinese/index.html', context)
