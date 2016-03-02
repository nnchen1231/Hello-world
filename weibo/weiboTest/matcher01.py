#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nnchen1231'

import re
import tool
#处理编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def matcher01(pages):
    i = 1
    reg = r'<div class=\\"WB_cardwrap S_bg2 clearfix\\" >[\s\S]*?<div mid=\\"(.*?)\\".*?>[\s\S]*?<div class=\\"face\\">[\s\S]*?href=\\"(.*?)\\" title=\\"(.*?)\\".*?>'  #获得id,用户名和url
    reg = r'<p class=\\"comment_txt\\".*?>([\s\S]*?)<\\/p>' #获得微博内容
    reg = r'<div class=\\"feed_from W_textb\\">.*?<a href=\\"(.*?)\\".*?title=\\"(.*?)\\"[\s\S]*?<a target=\\"_blank\\".*?>(.*?)<\\/a>'  #获得微博页面url，微波的发布时间和微波的来源
    reg = r'<div class=\\"feed_action clearfix\\">[\s\S]*?action-type=\\"feed_list_forward\\".*?>(.*?)<\\/span>[\s\S]*?action-type=\\"feed_list_comment\\".*?>(.*?)<\\/span>[\s\S]*?action-type=\\"feed_list_like\\".*?>(.*?)<\\/span>'  #获得微博的转发，评论，点赞数量
    reg=re.compile(reg)
    mats=reg.findall(pages)
    if mats!='[]':
        for mat in mats:
            #输出id,用户名和url
            # id = mat[0]
            # url =  mat[1].replace('\\','')
            # name = eval('u"'+mat[2]+'"')
            # print i,name,url,id
            #输出微博内容
            # comment = eval('u"'+mat+'"')
            # comment = tool.Tool().replace(comment)
            # print i,comment
            #输出微博页面url，微波的发布时间和微波的来源
            # weiboUrl = mat[0].replace('\\','')
            # weiboTime = mat[1]
            # weiboFrom = eval('u"'+mat[2]+'"')
            # print i,weiboUrl,weiboTime,weiboFrom
            #输出微博的转发，评论，点赞数量
            forwardNum = tool.Tool().replace(mat[0])
            forwardNum = eval('u"'+forwardNum+'"')
            forwardNum = forwardNum.replace('转发','')
            commentNum = tool.Tool().replace(mat[1])
            commentNum = eval('u"'+commentNum+'"')
            commentNum = commentNum.replace('评论','')
            likeNum = tool.Tool().replace(mat[2])
            likeNum = eval('u"'+likeNum+'"')
            if forwardNum=='':
                forwardNum = 0
            if commentNum=='':
                commentNum=0
            if likeNum=='':
                likeNum=0
            print i,forwardNum,commentNum,likeNum
            i +=1



def getText():
    f = open('test01','r')
    #print f.read()
    return f.read()




if __name__=='__main__':
    pages = getText()
    matcher01(pages)