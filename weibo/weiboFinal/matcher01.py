#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nnchen1231'

import re
import MySQLdb
import tool
import md5
import getCommments
#处理编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Matcher01:
    #初始化一些变量
    def __init__(self,para,pages):
        self.para = para
        self.pages = pages
        self.tool = tool.Tool()

    def pageAnalyse(self):
        contents = []
        # reg = r'<div class=\\"WB_cardwrap S_bg2 clearfix\\" >[\s\S]*?<div mid=\\"(.*?)\\".*?>[\s\S]*?<div class=\\"face\\">[\s\S]*?href=\\"(.*?)\\" title=\\"(.*?)\\".*?>'  #获得id,用户名和url
        # reg = r'<p class=\\"comment_txt\\".*?>([\s\S]*?)<\\/p>' #获得微博内容
        # reg = r'<div class=\\"feed_from W_textb\\">.*?<a href=\\"(.*?)\\".*?title=\\"(.*?)\\"[\s\S]*?<a target=\\"_blank\\".*?>(.*?)<\\/a>'  #获得微博页面url，微波的发布时间和微波的来源
        # reg = r'<div class=\\"feed_action clearfix\\">[\s\S]*?action-type=\\"feed_list_forward\\".*?>(.*?)<\\/span>[\s\S]*?action-type=\\"feed_list_comment\\".*?>(.*?)<\\/span>[\s\S]*?action-type=\\"feed_list_like\\".*?>(.*?)<\\/span>'  #获得微博的转发，评论，点赞数量
        #用正则表达式匹配出该条微薄的用户名，主页url，id，内容，发布时间等
        reg01 = r'<div class=\\"WB_cardwrap S_bg2 clearfix\\" >[\s\S]*?<div mid=\\"(.*?)\\".*?>[\s\S]*?<div class=\\"face\\">[\s\S]*?href=\\"(.*?)\\" title=\\"(.*?)\\".*?>[\s\S]*?' \
              r'<p class=\\"comment_txt\\".*?>([\s\S]*?)<\\/p>[\s\S]*?' \
              r'<div class=\\"feed_from W_textb\\">.*?<a href=\\"(.*?)\\".*?title=\\"(.*?)\\"[\s\S]*?<a target=\\"_blank\\".*?>(.*?)<\\/a>[\s\S]*?'
        #获得微薄的转发数，评论数，点赞数
        reg02 = r'<div class=\\"feed_action clearfix\\">[\s\S]*?action-type=\\"feed_list_forward\\".*?>(.*?)<\\/span>[\s\S]*?action-type=\\"feed_list_comment\\".*?>(.*?)<\\/span>[\s\S]*?action-type=\\"feed_list_like\\".*?>(.*?)<\\/span>'
        reg01=re.compile(reg01)
        reg02=re.compile(reg02)
        mats01=reg01.findall(self.pages)
        mats02=reg02.findall(self.pages)
        for i in range(min(len(mats01),len(mats02))):
            mat = mats01[i]+mats02[i]
            userId = mat[0]  #用户id
            userUrl = mat[1].replace('\\','')   #用户主页url
            userName = eval('u"'+mat[2]+'"')   #用户昵称
            weiboContent = eval('u"'+mat[3]+'"')    #微波内容
            weiboContent = tool.Tool().replace(weiboContent)   #
            weiboUrl = mat[4].replace('\\','')    #微波Url
            weiboTime = mat[5]    #微波发布时间
            weiboFrom = eval('u"'+mat[6]+'"')    #微波发送的方式
            forwardNum = tool.Tool().replace(mat[7])   #微波的转发数量
            forwardNum = eval('u"'+forwardNum+'"')
            forwardNum = forwardNum.replace('转发','')
            commentNum = tool.Tool().replace(mat[8])   #微薄的评论数量
            commentNum = eval('u"'+commentNum+'"')
            commentNum = commentNum.replace('评论','')
            likeNum = tool.Tool().replace(mat[9])    #微波的点赞数量
            likeNum = eval('u"'+likeNum+'"')
            if forwardNum=='':
                forwardNum = 0
            if commentNum=='':
                commentNum=0
            if likeNum=='':
                likeNum=0
            str01 = str(id) + str(userName) + str(weiboContent) + str(weiboTime)
            weiboMd5 =  md5.md5(str01)
            contents.append((weiboMd5,userName,userUrl,weiboTime,weiboFrom,userId,weiboContent,weiboUrl,self.para,forwardNum,commentNum,likeNum))
            print i+1,u'\tMd5：',weiboMd5,u'\t昵称：',userName,u'\t主页Url：',userUrl,u'\tId:',userId,u'\n内容：',weiboContent,\
                u'\n发布时间：',weiboTime,u'\t终端：',weiboFrom,u'\t微博url：',weiboUrl,\
                u'\n转发数：',forwardNum,u'\t评论数：',commentNum,u'\t点赞数：',likeNum,'\n'
            getCommments.Comments(userId).start()
            i += 1
        return contents

    def insertContents(self):
        try:
            contents = self.pageAnalyse()
            conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='nopasite',charset='utf8')
            cur = conn.cursor()
            cur.execute("select weibo_md5 from weibo")
            weiboMD5 = cur.fetchall()
            #将元组转化为str
            weiboMD5 = weiboMD5.__str__()
            for content in contents:
                if content[0] in weiboMD5:
                    print content[0] + u'已经存在'
                    continue
                else:
                    cur.execute("insert into weibo(weibo_md5,weibo_name,weibo_homepage,weibo_time,weibo_from,weibo_id,weibo_content,weibo_url,weibo_keywords,weibo_forwarding,weibo_comment,weibo_like) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",content)
                    conn.commit()
                    print u'插入成功'
            cur.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])


# def getText():
#     f = open('test_chen','r')
#     #print f.read()
#     return f.read()
#
# if __name__=='__main__':
#     pages = getText()
#     Matcher01(123,pages).pageAnalyse()