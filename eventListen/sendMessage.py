#! /usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import json



CORPID      = 'wx7ad7d1c3e3e5d30c'
CORPSECRET  = 'IAiXx4qeqZVlzhCwS0dWDH2C0SYNhLVy6ltCxtbM1VuyHPnuJM3i3ENicGaI0sjk'
TOKEN_URL   = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
MESSAGE_URL = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token'

#--------------------#
# 获取token           #
#--------------------#
def get_token():
    values = {
        'corpid'    : CORPID,
        'corpsecret': CORPSECRET,
    }
    req  = requests.post(TOKEN_URL, params=values)
    data = json.loads(req.text)
    return data["access_token"]


# ---------------------#
# data : 发送的信息   #
# app_id: 应用id      #
# part_id: 分组id     #
# ---------------------#
def send_msg(data, app_id, part_id):
    url    = '+'.join([MESSAGE_URL, get_token()])
    values = {
        'toparty': "%s" % (part_id),
        'msgtype': "text",
        'agentid': app_id,
        'text': {
            'content': data
        }
    }
    # data = json.dumps(values, ensure_ascii=False)
    # return json.dumps(values, ensure_ascii=False)
    req = requests.post(url, json.dumps(values, ensure_ascii=False))
    return req.text


