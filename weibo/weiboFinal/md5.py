# -*- encoding:utf-8 -*-
__author__ = 'nnchen1231'

import hashlib
import types

def md5(str):
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''

#str = '123'
#print md5(str)