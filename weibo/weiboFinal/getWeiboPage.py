#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nnchen1231'

import re
import urllib
import urllib2
import time
import matcher
#处理编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class getWeiboPage:
    #初始化变量
    def __init__(self,category,i):
        self.category = category
        self.i = i
        self.reg01 = re.compile(r'咦？暂时没有内容哦，稍后再来试试吧~~')
        self.reg02 = re.compile(r'\\u54a6\\uff1f\\u6682\\u65f6\\u6ca1\\u6709\\u5185\\u5bb9\\u54e6\\uff0c\\u7a0d\\u540e\\u518d\\u6765\\u8bd5\\u8bd5\\u5427~~')

    def get_firstpage(self):
        url01 = 'http://d.weibo.com/'+ str(self.category) + '?current_page=3&since_id=&page=' + str(self.i) + '#feedtop'
        print u'正在获取第' + str(self.i) + '页，第一部分内容'
        response = urllib2.urlopen(url01)
        #print response.read()
        for page in response:
            if re.search(r'"pl.content.homeFeed.index"',page):    #匹配一定要准确！！!   "pid":"pl_weibo_direct"
                if self.reg01.search(page):
                    print u'咦？暂时没有内容哦，稍后再来试试吧~~'
                    return 0
                else:
                    # print line
                    # matcher.matcher(line).pageAnalyse()
                    return page

    def get_secondpage(self):
        url02 = 'http://d.weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=' + str(self.category) + '&current_page=1&since_id=&page=' + str(self.i) + '&pre_page=' + str(self.i) + '&max_id=&end_id=&pagebar=0&filtered_min_id=&pl_name=Pl_Core_MixedFeed__5&id='+ str(self.category) + '&script_uri=/'+ str(self.category) + '&feed_type=1&tab=home&domain_op='+ str(self.category) + '&__rnd='
        print u'正在获取第' + str(self.i) + '页，第二部分内容'
        req = urllib2.Request(url02)
        result = urllib2.urlopen(req)
        page = result.read()
        #print result.read()
        if self.reg02.search(page):
            print u'咦？暂时没有内容哦，稍后再来试试吧~~'
            return 0
        else:
            return page
        #matcher.matcher(result.read()).pageAnalyse()

    def get_thirdpage(self):
        url03 = 'http://d.weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=' + str(self.category) + '&current_page=1&since_id=&page=' + str(self.i) + '&pre_page=' + str(self.i) + '&max_id=&end_id=&pagebar=1&filtered_min_id=&pl_name=Pl_Core_MixedFeed__5&id='+ str(self.category) + '&script_uri=/'+ str(self.category) + '&feed_type=1&tab=home&domain_op='+ str(self.category) + '&__rnd='
        print u'正在获取第' + str(self.i) + '页，第三部分内容'
        req = urllib2.Request(url03)
        result = urllib2.urlopen(req)
        page = result.read()
        #print result.read()
        if self.reg02.search(page):
            print u'咦？暂时没有内容哦，稍后再来试试吧~~'
            return 0
        else:
            return page
        #matcher.matcher(result.read()).pageAnalyse()