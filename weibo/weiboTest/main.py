# -*- coding: utf-8 -*-
__author__ = 'nnchen1231'
import urllib2
import weiboLogin


#filename = './config/account'#保存微博账号的用户名和密码，第一行为用户名，第二行为密码

username = 'nnchen1231@163.com'
pwd = 'nan18756072542'
WBLogin = weiboLogin.weiboLogin()
if WBLogin.login(username,pwd)==1:
    print 'Login success!'
else:
    print 'Login error!'
    exit()

url = 'http://d.weibo.com/102803_ctg1_4188_-_ctg1_4188?from=faxian_hot&mod=fenlei#'
#req = urllib2.Request(url)
response = urllib2.urlopen(url)
for line in response:
    print line
#print response.read()
# req = urllib2.Request(url)
# response = urllib2.urlopen(url)
# print response.read()