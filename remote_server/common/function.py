# -*- coding:utf-8 -*-
# from elasticsearch import Elasticsearch
from django.http import HttpResponse, JsonResponse
# from security_system.settings import ES_CONN_CONFIG

#
# def createConnectes():
#     """
#     用于连接ES
#     """
#     es = Elasticsearch([ES_CONN_CONFIG,])
#     return es


def success_msg(msg_detail=None):
    """"
    构造一个用于返回页面成功的消息

    """
    r={'result':'successs'}

    if msg_detail:
        r['detail']=msg_detail
    else:
        r['detail']={}

    return r



def error_msg(err_code, err_msg):
    """
    构造一个用于返回给页面的错误消息
    :param err_code:
    :param err_msg:
    :return: dict
    """
    r = {'result': 'error',
         'detail': {
             'error_code': err_code,
             'error_msg': err_msg
         }}
    return r

def error_msg_list(msg_list):
    """
    当API是对多个项目进行操作时，使用此方法可以返回一个错误列表给页面
    :param msg_list:
    :return: dict
    """
    assert isinstance(msg_list, list)
    r = {'result': 'error',
         'detail': {
             'errors': msg_list
         }}
    return r

def json_response(msg, ensure_ascii=False):
    """
    给django的JsonResponse增加中文编码支持
    :param ensure_ascii:
    :param msg:
    :return:
    """
    dumps_params = {'ensure_ascii': False}
    return JsonResponse(msg, json_dumps_params=dumps_params)
