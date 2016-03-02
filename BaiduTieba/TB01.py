#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nnchen1231'

import urllib
import urllib2
import re
from bs4 import BeautifulSoup

url='http://bbs.tianya.cn/'
try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    print content
    # #print content
    # #soup = BeautifulSoup(content)
    # #print soup.prettify()
    # #for child in  soup.body.children:
    # #    print child
    # pattern = re.compile('<div class="item fore.*?a">.*?'
		# 				'<h3>(.*?)(.*?)</h3>.*?</div>',re.S)
    # items = re.findall(pattern,content)
    # for item in items:
    #     p=item[1]
    #     pat=re.compile('<a target="_blank" href="(.*?)">(.*?)</a>')
    #     i=re.findall(pat,p)
    #     for e in i:
    #             print e[1],e[0]
    #     #print item[1]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

