'''
Created on 2015-6-3

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''

import memcache

from mainsite.models import VisitInfo
from django.conf import settings


def do_collect():
    mc = memcache.Client([settings.MEMCACHE_HOST])
    count_num = mc.get(settings.COUNTER_KEY)
    if count_num == None:
        count_num = 0
    # record into db
    visit_info = VisitInfo(number=count_num, type='daily', page='')
    visit_info.save()
    # after record, clean cache data
    mc.set(settings.COUNTER_KEY, 0)


def run(*args):
    do_collect()
