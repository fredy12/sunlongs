'''
Created on 2015-6-3

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''
import json
import time
from pika import ConnectionParameters, BlockingConnection

from reporter.models import TestRecord
from reporter.oss_notification import OSS_Connect


def do_collect(body):
    print 'receive msg is: %s' % body
    test_record_info = json.loads(body)
    tr = TestRecord(test_type=test_record_info['test_type'],
                    test_uuid=test_record_info['test_uuid'],
                    test_env=test_record_info['test_env'],
                    start_test_time=test_record_info['start_test_time'],
                    stop_test_time=test_record_info['stop_test_time'],
                    duration=test_record_info['duration'],
                    test_content=json.dumps(test_record_info['test_content']))
    tr.save()


def do_mq_collect(channel, method_frame, header_frame, body):
    do_collect(body)
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)


RABBITMQ_HOST = 'ecstest.alibaba-inc.com'
RABBITMQ_QUEUE = 'ecs-report'
def listen_mq():
    connection = BlockingConnection(ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.basic_consume(do_mq_collect, RABBITMQ_QUEUE)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()


def do_mq_show():
    pass


def do_mq_clean():
    pass


OSS_HOST = 'oss-cn-hangzhou-zmf.aliyuncs.com'
ACCESS_ID = 'yIeORo0BpoVqHrwt'
ACCESS_KEY = 'DT6GakO4vX8rbIQoBXpubkb2ZdR7hn'
BUCKET_NAME = 'ecs-report'
def listen_oss():
    oss_conn = OSS_Connect(OSS_HOST, ACCESS_ID, ACCESS_KEY)
    while True:
        obj_list = oss_conn.get_object_name_list_of_bucket(BUCKET_NAME)
        for obj_name in obj_list:
            obj_content = oss_conn.get_object_content(BUCKET_NAME, obj_name)
            do_collect(obj_content)
            oss_conn.delete_object(BUCKET_NAME, obj_name)
        time.sleep(10)


def do_oss_show():
    oss_conn = OSS_Connect(OSS_HOST, ACCESS_ID, ACCESS_KEY)
    obj_list = oss_conn.get_object_name_list_of_bucket(BUCKET_NAME)
    print 'ALL object in OSS bucket ecs_report is %s' % obj_list


def do_oss_clean():
    oss_conn = OSS_Connect(OSS_HOST, ACCESS_ID, ACCESS_KEY)
    obj_list = oss_conn.get_object_name_list_of_bucket(BUCKET_NAME)
    for obj_name in obj_list:
        oss_conn.delete_object(BUCKET_NAME, obj_name)
    print oss_conn.get_bucket(BUCKET_NAME).read()
    print 'DONE'


def run(*args):
    if 'clean' in args:
        if 'mq' in args:
            do_mq_clean()
        else:
            do_oss_clean()
        return
    if 'show' in args:
        if 'mq' in args:
            do_mq_show()
        else:
            do_oss_show()
    if 'oss' in args:
        listen_oss()
    if 'mq' in args:
        listen_mq()
