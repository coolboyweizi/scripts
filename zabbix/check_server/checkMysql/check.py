#!/usr/bin/env python
# coding:utf-8
import json
import sys

# 用于业务机远程连接信息
port_list = {
    'fr-db-cms': ['fr-db:3306','sing_cms','fB5e5f#46)5"aa']
}

# 用于服务器监控指标。
items = ['Bytes_received', 'Bytes_sent', 'Questions','Slow_queries']

# 获取数据库连接可连接列表
def getInfo():
    value = list()
    for key,item in port_list.items():
        value.append({"{#SERVER}": key, "{#auth}": item.pop(), "{#PORTS}": ":".join(item)})

    return json.dumps({"data":value})

# 获取服务器性能数据
def getItem():
    value = list()
    for key in port_list.keys():
        for item in items:
            value.append({"{#SERVER}":key,"{#ITEM}":item})
    return json.dumps({"data": value})

if __name__ == '__main__':
    if sys.argv[1] == 'item':
        print getItem()
    else:
        print getInfo()


