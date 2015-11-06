# -*- coding: utf-8 -*-
'''
Created on 2015-9-23

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''

from mainsite.lib.utils import reject_not_slongpump
from django.http.response import HttpResponseRedirect


# Create your views here.
@reject_not_slongpump
def index(request):
    return HttpResponseRedirect('cn/index.html')

