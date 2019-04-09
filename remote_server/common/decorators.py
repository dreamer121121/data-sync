# -*- coding:utf-8 -*-
#
# 装饰器
#
import hmac
import json
import logging
import time
from functools import wraps

from django.contrib.auth.models import Permission, User
from django.shortcuts import HttpResponse
from django.utils import six

from common.error_code import E001
from common.function import json_response, error_msg
from common.function import success_msg, json_response, error_msg

logger = logging.getLogger(__name__)
perf_logger = logging.getLogger('performance')


def http_method_required(method):
    """
    http请求必须是给定的method, 否则返回错误消息
    """

    def _deco(func):
        @wraps(func)
        def __wrapper(*args, **kwargs):

            if args[0].method == method:
                return func(*args, **kwargs)
            else:
                msg = E001.msg % (args[0].method, method)
                logger.error(msg)
                r = error_msg(E001.code, msg)
                return json_response(r)

        return __wrapper

    return _deco


