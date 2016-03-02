#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nnchen1231'

import urllib
import urllib2
import time
import re
import weiboLogin
import tool
#处理编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Comments:
    def __init__(self,id):
        self.id = id
        self.tool = tool.Tool()
        self.defaultTitle = u"新浪微博"
        #楼层标号，初始为1
        self.floor = 1
        #评论数目，初始为1
        self.num = 1
        #还没有人评论，赶快抢个沙发
        self.reg01 = re.compile(r'\\u8fd8\\u6ca1\\u6709\\u4eba\\u8bc4\\u8bba\\uff0c\\u8d76\\u5feb\\u62a2\\u4e2a\\u6c99\\u53d1')
        #为了避免骚扰，微博智能反垃圾系统会过滤掉部分广告用户。
        self.reg02 = re.compile(r'\\u4e3a\\u4e86\\u907f\\u514d\\u9a9a\\u6270\\uff0c\\u5fae\\u535a\\u667a\\u80fd\\u53cd\\u5783\\u573e\\u7cfb\\u7edf\\u4f1a\\u8fc7\\u6ee4\\u6389\\u90e8\\u5206\\u5e7f\\u544a\\u7528\\u6237\\u3002')

    def getPages(self,pageNum):
        try:
            url = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id=' + str(self.id) + '&max_id=&page=' + str(pageNum) + '&__rnd='
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            pages = response.read()
            #print pages
            # if self.reg01.search(pages) :
            #     print u'还没有人评论，赶快抢个沙发'
            #     return  0
            # else:
            #     return pages
            return pages
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"评论页面链接失败,错误原因",e.reason
                return None

    #获取评论页面的页数totalpage，评论的条数
    def getPageNum(self,page):
        pattren = re.compile(r'"page":\{"totalpage":(.*?),"pagenum":1\},"count":(.*?)\}')
        result = re.search(pattren,page)
        if result:
            totalpage = result.group(1)
            count = result.group(2)
            #print totalpage,count
            return totalpage,count
        else:
            return

    def setFileTitle(self):
        self.file = open(self.defaultTitle + ".txt","w+")

    def writeData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
            self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1

    def pageAnalyse(self,page):
        comments = []
        # i = 1
        # while True:
        #     print u'正在获取第'  + str(i) + u'页'
        #     pages = self.getPages(i)
        #     if pages == 0:
        #         break
        reg = r'<div comment_id=.*?>.*?<div class=\\"WB_text\\">.*?<.*?href=\\"\\(.*?)\\".*?>(.*?)<\\/a>(.*?)<\\/div>.*?action-type=\\"fl_like\\".*?>(.*?)<\\/a>'
        reg = re.compile(reg)
        mats=reg.findall(page)
        for mat in mats:
            user = self.tool.replace(eval('u"'+mat[1]+'"'))
            userUrl = 'http://weibo.com/u/' + mat[0]
            comment = self.tool.replace(eval('u"'+mat[2]+'"'))
            likeNum = self.tool.replace(eval('u"'+mat[3]+'"'))
            if likeNum =='':
                likeNum = 0
            #print 'http://weibo.com/u/' + mat[0],self.tool.replace(eval('u"'+mat[1]+'"')),self.tool.replace(eval('u"'+mat[2]+'"')),self.tool.replace(eval('u"'+mat[3]+'"'))
            print self.num,u'评论者：', user ,u'\t主页：',userUrl , '\n评论内容：',comment, '\t点赞数：',likeNum,'\n'
            comments.append(comment)
            self.num += 1
        #i += 1
        time.sleep(5)
        return comments

    def start(self):
        indexPage = self.getPages(1)
        pageNum,count = self.getPageNum(indexPage)
        #self.setFileTitle()
        if int(count) == 0:
            print "该条微博暂时还没有评论，请继续下一条、、、"
            return
        else:
            print "该条微博共有" + str(pageNum) + "页评论"
            for i in range(1,int(pageNum)+1):
                print "正在获取第" + str(i) + "页评论"
                page = self.getPages(i)
                comments = self.pageAnalyse(page)
                #self.writeData(comments)


if __name__ =='__main__':
    username = 'nnchen1231@163.com'
    pwd = 'nan18756072542'
    id = raw_input('请输入微博Id：\n')
    WBLogin = weiboLogin.weiboLogin()
    if WBLogin.login(username,pwd)==1:
        print 'Login success!'
        #Comments(id).pageAnalyse()
        Comments(id).start()