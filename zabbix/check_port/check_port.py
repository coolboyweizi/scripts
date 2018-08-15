#!/usr/bin/env python
# coding:utf-8

import socket, sys
HOSTNAME='test'

try:
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = sys.argv[2].split()[0]
    port = int(sys.argv[2].split()[1])
    # 设置超时时间（0.0）
    sc.settimeout(5)
    sc.connect((ip, port))
    sc.close()
    print 1
except:
    print 0