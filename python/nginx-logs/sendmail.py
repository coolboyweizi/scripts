#!/usr/bin/env python
#coding:utf-8
# User: MK
# Desc: 邮件系统
import sys
import smtplib
from email.mime.text import MIMEText
import datetime

def getYesterday():
  today=datetime.date.today()
  oneday=datetime.timedelta(days=1)
  yesterday=today-oneday
  return yesterday


HOST = {
    'server':'47.90.83.225',
    'port':28825,
}

TO = 'demo@qq.com'
FROM='dailywork@qq.com'
TITLE  = 'api服务器'
SUBJECT = 'api每日访问数据'


# <tr><td>localhost</td><td>5</td><td>POST</td><td>test</td></tr>

TDSTR = '<center>%s daily pv at %s </center>' %(TITLE, getYesterday())
while True:

    date = sys.stdin.readline()
    if not date : break
    d = date.split()

    TDSTR += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' \
    %(''.join((TITLE, d[1])),d[0],d[2],d[3],d[4])

TEXT = MIMEText(
    """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>每日访问统计</title>
    <style>
        th,td {
            text-align: center;
            border: 1px solid #CCCCCC;
        }
    </style>
</head>
<body>
<table width="600" style="margin: auto" cellpadding="0"  cellspacing="0">
    <tr>
        <th>URI</th><th>次数</th><th>Method</th><th>app0</th><th>app1</th>
    </tr>

    %s

</table>

</body>
</html>

    """ %TDSTR,
    "html",
    "utf-8"
)

TEXT['Subject'] = SUBJECT
TEXT['From']    = FROM
TEXT['To']      = TO


server= smtplib.SMTP()
server.connect(HOST['server'], HOST['port'])
Counter = 10
while Counter > 0 :
    print Counter
    try:
        server.connect(HOST['server'], HOST['port'])
        server.login('dailywork@qq.cc','email_password')
        server.sendmail(
            FROM,
            TO.split(";"),
            TEXT.as_string()
        )
        print 'has sent'
        Counter = 0
        server.quit()
    except BaseException,e:
        print e
        Counter -= 1


