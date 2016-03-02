#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nnchen1231'

import urllib
import urllib2
import time
import weiboLogin
import getWeiboPage
import matcher

def main():
    categorys = ['102803_ctg1_4188_-_ctg1_4188','102803_ctg1_2088_-_ctg1_2088','102803_ctg1_5988_-_ctg1_5988','102803_ctg1_5088_-_ctg1_5088','102803_ctg1_1288_-_ctg1_1288','102803_ctg1_4288_-_ctg1_4288',
                 '102803_ctg1_4688_-_ctg1_4688','102803_ctg1_2488_-_ctg1_2488','102803_ctg1_3288_-_ctg1_3288','102803_ctg1_5288_-_ctg1_5288','102803_ctg1_5188_-_ctg1_5188','102803_ctg1_1388_-_ctg1_1388',
                 '102803_ctg1_4788_-_ctg1_4788','102803_ctg1_2188_-_ctg1_2188','102803_ctg1_6088_-_ctg1_6088','102803_ctg1_1199_-_ctg1_1199','102803_ctg1_2288_-_ctg1_2288','102803_ctg1_4988_-_ctg1_4988',
                 '102803_ctg1_1988_-_ctg1_1988','102803_ctg1_4388_-_ctg1_4388','102803_ctg1_5788_-_ctg1_5788','102803_ctg1_4888_-_ctg1_4888','102803_ctg1_2588_-_ctg1_2588','102803_ctg1_3188_-_ctg1_3188',
                 '102803_ctg1_1488_-_ctg1_1488','102803_ctg1_2688_-_ctg1_2688','102803_ctg1_5588_-_ctg1_5588','102803_ctg1_5888_-_ctg1_5888','102803_ctg1_1688_-_ctg1_1688','102803_ctg1_4588_-_ctg1_4588',
                 '102803_ctg1_5388_-_ctg1_5388','102803_ctg1_5488_-_ctg1_5488','102803_ctg1_4488_-_ctg1_4488','102803_ctg1_1588_-_ctg1_1588','102803_ctg1_2388_-_ctg1_2388','102803_ctg1_5688_-_ctg1_5688',
                 '102803_ctg1_6399_-_ctg1_6399','102803_ctg1_2788_-_ctg1_2788']
    categorys = ['102803_ctg1_1199_-_ctg1_1199']   #需要修改
    categorys = ['102803_ctg1_2288_-_ctg1_2288','102803_ctg1_4988_-_ctg1_4988',
                 '102803_ctg1_1988_-_ctg1_1988','102803_ctg1_4388_-_ctg1_4388','102803_ctg1_5788_-_ctg1_5788','102803_ctg1_4888_-_ctg1_4888','102803_ctg1_2588_-_ctg1_2588','102803_ctg1_3188_-_ctg1_3188',
                 '102803_ctg1_1488_-_ctg1_1488','102803_ctg1_2688_-_ctg1_2688','102803_ctg1_5588_-_ctg1_5588','102803_ctg1_5888_-_ctg1_5888','102803_ctg1_1688_-_ctg1_1688','102803_ctg1_4588_-_ctg1_4588',
                 '102803_ctg1_5388_-_ctg1_5388','102803_ctg1_5488_-_ctg1_5488','102803_ctg1_4488_-_ctg1_4488','102803_ctg1_1588_-_ctg1_1588','102803_ctg1_2388_-_ctg1_2388','102803_ctg1_5688_-_ctg1_5688',
                 '102803_ctg1_6399_-_ctg1_6399','102803_ctg1_2788_-_ctg1_2788']
    categorys = ['102803_ctg1_5688_-_ctg1_5688']
    username = 'nnchen1231@163.com'
    pwd = 'nan18756072542'
    WBLogin = weiboLogin.weiboLogin()
    if WBLogin.login(username,pwd)==1:
        print 'Login success!'
        for category in categorys:
            i = 1
            while True:
                print u'正在获取第' + str(i) + '页内容、、、'
                page01 = getWeiboPage.getWeiboPage(category,i).get_firstpage()
                if page01 == 0:
                    break
                else:
                    #matcher.matcher(page01).pageAnalyse()
                    matcher.matcher(page01).insertContents()
                time.sleep(5)
                page02 = getWeiboPage.getWeiboPage(category,i).get_secondpage()
                if page02 == 0:
                    break
                else:
                    #matcher.matcher(page02).pageAnalyse()
                    matcher.matcher(page02).insertContents()
                time.sleep(10)
                page03 = getWeiboPage.getWeiboPage(category,i).get_thirdpage()
                if page03 == 0:
                    break
                else:
                    #matcher.matcher(page03).pageAnalyse()
                    matcher.matcher(page03).insertContents()
                time.sleep(30)
                i += 1
            time.sleep(60)
    else:
        print 'Login error!'
        exit()
if __name__=='__main__':
    main()
