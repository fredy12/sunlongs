'''
Created on 2015-10-14

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''

import time
import memcache
import logging

from django.conf import settings
from django.http.response import HttpResponseRedirect


logger = logging.getLogger(__name__)


def get_remote_addr(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip_addr =  request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip_addr = request.META['REMOTE_ADDR']
    return ip_addr


def record_visit(func):
    def inner_func(*args, **kwargs):
        request = args[0]
        remote_addr = get_remote_addr(request)
        mc = memcache.Client([settings.MEMCACHE_HOST])
        visit_info = mc.get(remote_addr)
        if visit_info == None:
            # means first visit, record this visit (page name + time)
            mc.set(remote_addr, time.time())
            # the counter ++
            if mc.get(settings.COUNTER_KEY) == None:
                mc.set(settings.COUNTER_KEY, 0)
            mc.incr(settings.COUNTER_KEY)
            logger.debug('visitor [%s] with a new visit, counter ++ , now counter is [%s]' % (remote_addr, mc.get(settings.COUNTER_KEY)))
        else:
            if time.time() - visit_info > 24 * 3600:
                # means visitor with a new visit, counter ++, record this visit
                mc.set(remote_addr, time.time())
                if mc.get(settings.COUNTER_KEY) == None:
                    mc.set(settings.COUNTER_KEY, 0)
                mc.incr(settings.COUNTER_KEY)
                logger.debug('visitor [%s] with a expired new visit, counter ++ , now counter is [%s]' % (remote_addr, mc.get(settings.COUNTER_KEY)))
            else:
                # means visitor has already visited
                pass
        print mc.get(settings.COUNTER_KEY)
        return func(*args, **kwargs)
    return inner_func


def reject_not_slongpump(func):
    def inner_func(*args, **kwargs):
        #request = args[0]
        #if request.get_host() != 'www.slongpump.com':
        #    return HttpResponseRedirect('http://www.slongpump.com/cn/index.html')
        return func(*args, **kwargs)
    return inner_func

