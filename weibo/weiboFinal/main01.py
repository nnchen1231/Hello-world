#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nnchen1231'

import re
import time
import random
import urllib2
import weiboLogin
import matcher01

def main():
    urlheader='http://s.weibo.com/weibo/'
    para=raw_input('请输入搜索内容：\n')
    if ' ' in para:
        keywords = para.replace(' ','%20')
    else:
        keywords = para
    print keywords
    page = 1
    reg1=re.compile(r'\\u4f60\\u7684\\u884c\\u4e3a\\u6709\\u4e9b\\u5f02\\u5e38\\uff0c\\u8bf7\\u8f93\\u5165\\u9a8c\\u8bc1\\u7801\\uff1a')    #你的行为有些异常，请输入验证码
    reg2=re.compile(r'\\u62b1\\u6b49\\uff0c\\u672a\\u627e\\u5230')#抱歉，未找到搜索结果
    username = 'nnchen1231@163.com'
    username = '377759578@qq.com'
    pwd = 'nan18756072542'
    WBLogin = weiboLogin.weiboLogin()
    if WBLogin.login(username,pwd)==1:
        print '登录成功。。。'
        user=True    #帐号可用

    while page<=50 and user:
        url=urlheader+keywords+'&page='+str(page)
        print '获取第%d页。。' % page
        f=urllib2.urlopen(url)
        #print f.read()
        ###开始匹配网页内容###
        for line in f:
            if re.search(r'pid":"pl_weibo_direct"',line):    #匹配一定要准确！！!   "pid":"pl_weibo_direct"
                print line
                if reg2.search(line):
                    print '抱歉，未找到结果。。。'
                    return
                else:
                    page += 1
                    #matcher01.Matcher01(para,line).pageAnalyse()
                    matcher01.Matcher01(para,line).insertContents()
                    stop = random.randint(0,120)
                    print stop
                    time.sleep(stop)
                    break
            if re.search(r'"pid":"pl_common_sassfilter"',line):   #"pid":"pl_common_sassfilter"
                if reg1.search(line):
                    print '此帐号被锁，使用下一个帐号'
                    user=False    #帐号不可用


if __name__=='__main__':
    main()
