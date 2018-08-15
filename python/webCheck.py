#! /usr/bin/python
# coding:utf-8
# -*- coding : utf-8 -*-

import sys, pycurl

request_url = sys.argv[1]
curl_obj = pycurl.Curl()
# 创建一个curl对象

curl_obj.setopt(pycurl.CONNECTTIMEOUT, 5)
# 连接的等待时间,设置为0则不等待
curl_obj.setopt(pycurl.TIMEOUT, 5)
# 最大下載时间
curl_obj.setopt(pycurl.NOPROGRESS, 1)
# 是否屏蔽下载进度条,非0则屏蔽
curl_obj.setopt(pycurl.MAXREDIRS, 0)
# 指定HTTP重定向的最大数
curl_obj.setopt(pycurl.FORBID_REUSE, 1)
# 完成交互后强制断开连接,不重用
curl_obj.setopt(pycurl.FRESH_CONNECT, 1)
# 强制获取新的连接,即替代缓存中的连接
curl_obj.setopt(pycurl.DNS_CACHE_TIMEOUT, 1)
# 设置保存DNS信息的时间,默认为120秒
curl_obj.setopt(pycurl.URL, request_url)
# 指定请求的URL

import StringIO

strio = StringIO.StringIO()
curl_obj.setopt(pycurl.WRITEFUNCTION, strio.write)

try:
    curl_obj.perform()
    err_mess = ''
except Exception as e:
    err_mess = str(e)
# 访问页面

total_time = curl_obj.getinfo(pycurl.TOTAL_TIME)
# 传输结束所消耗的总时间
dns_time = curl_obj.getinfo(pycurl.NAMELOOKUP_TIME)
# 从发起请求到DNS解析完成所消耗的时间
connect_time = curl_obj.getinfo(pycurl.CONNECT_TIME)
# 从发起请求到建立连接所消耗的时间
redirect_time = curl_obj.getinfo(pycurl.REDIRECT_TIME)
# 从发起请求到重定向所消耗的时间
ssl_time = curl_obj.getinfo(pycurl.APPCONNECT_TIME)
# 从发起请求到SSL建立握手时间
pretrans_time = curl_obj.getinfo(pycurl.PRETRANSFER_TIME)
# 从发起请求到准备传输所消耗的时间
starttrans_time = curl_obj.getinfo(pycurl.STARTTRANSFER_TIME)
# 从发起请求到接收第一个字节的时间

print '发起请求到DNS解析时间 : %.3f ms' % (dns_time * 1000)
print '发起请求到TCP连接完成时间: %.3f ms' % (connect_time * 1000)
print '发起请求到跳转完成时间: %.3f ms' % (redirect_time * 1000)
print '发起请求到SSL建立完成时间 : %.3f ms' % (ssl_time * 1000)
print '发起请求到客户端发送请求时间： %.3f ms' % (pretrans_time * 1000)
print '发起请求到客户端接受首包时间: %.3f ms' % (starttrans_time * 1000)
print '总时间为: %.3f ms' % (total_time * 1000)
print ''

transfer_time = total_time - starttrans_time
# 传输时间
serverreq_time = starttrans_time - pretrans_time
# 服务器响应时间，包括网络传输时间
if ssl_time == 0:
    if redirect_time == 0:
        clientper_time = pretrans_time - connect_time
        # 客户端准备发送数据时间
        redirect_time = 0
    else:
        clientper_time = pretrans_time - redirect_time
        redirect_time = redirect_time - connect_time
    ssl_time = 0
else:
    clientper_time = pretrans_time - ssl_time

    if redirect_time == 0:
        ssl_time = ssl_time - connect_time
        redirect_time = 0
    else:
        ssl_time = ssl_time - redirect_time
        redirect_time = redirect_time - connect_time

connect_time = connect_time - dns_time

print '发起请求到DNS解析时间 : %.3f ms' % (dns_time * 1000)
print 'TCP连接消耗时间 : %.3f ms' % (connect_time * 1000)
print '跳转消耗时间: %.3f ms' % (redirect_time * 1000)
print 'SSL握手消耗时间 : %.3f ms' % (ssl_time * 1000)
print '客户端发送请求准备时间: %.3f ms' % (clientper_time * 1000)
print '服务器处理时间: %.3f ms' % (serverreq_time * 1000)
print '数据传输时间: %.3f ms' % (transfer_time * 1000)