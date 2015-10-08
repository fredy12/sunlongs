# -*- coding: utf-8 -*-
'''
Created on 2015-9-23

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''

from django.http.response import HttpResponseRedirect


# Create your views here.
def index(request):
    return HttpResponseRedirect('cn/index.html')

