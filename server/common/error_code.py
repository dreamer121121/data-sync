# -*- coding:utf-8 -*-
#
# 管理端错误码和错误消息
#


class Error(object):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg


# 注意：消息中带有%s符号

E000 = Error('ERR_S000', 'System Internal Error')
E001 = Error('ERR_S001', 'Invalid http method %s, need %s')


