#!/usr/bin/env python
#coding:utf-8
# User: mk
# Desc: nginx分析统计

import sys
import re


class Counter():
    def __init__(self):
        self.store = dict()

    def put(self, value):
        if self.store.has_key(value):
            self.store[value] += 1
        else:
            self.store[value] = 1

    def __getattr__(self, item):
        if self.store.has_key(item):
            return self.store[item]
        return 0


class RequestItem():
    def __init__(self, method, request, alias):
        '''
        请求数据对象
        :param method: 请求方法偏移量
        :param request: 请求body偏移量
        '''
        self.num = 0
        self.method  = method
        self.alias   = alias
        self.request = request
        self.RequestMethod  = Counter()
        self.RequestServer  = Counter()
        self.RequestBody    = Counter()

    def __str__(self):
        return str(self.num)

    def put(self, item):
        self.num += 1

        if self.method > 0 :
            method = item[self.method].upper()[1:]

            if method not in ['POST','GET']:return
            self.RequestMethod.put(method)


        if self.request > 0 :
            request = item[self.request]
            self.RequestBody.put(request)

        if self.alias > -1 :
            alias = item[self.alias]
            self.RequestServer.put(alias)

class RequestMain():
    def __init__(self):
        self.record = dict()

    def put(self, key, value):
        if self.record.has_key(key) == False:
            self.record[key] = RequestItem(5,8,0)
        self.record[key].put(value)



class Record():

    def __init__(self, offset):
        '''
        解析数据日志
        :param offset:      数据偏移量
        '''
        self.offsets  = offset
        self.extension= dict()

    def __iter__(self):
        return self

    def next(self):
        data = sys.stdin.readline()
        if not data:
            raise StopIteration
        return data.split()[self.offsets].split('?')[0],data.split()



if __name__ == '__main__':
    main = RequestMain()
    for record in Record(int(sys.argv[1])):
        if hasattr(  \
                re.match('^(/v[1-9]/|/api/|/c/page/)', record[0]), \
                'group') == False : continue

        main.put(record[0],record[1])

    #print type(main.record.items()[0][1].num)
    #record = sorted(main.record.items(),lambda key:key[1].num,reverse=True)
    mainRecord = sorted(main.record.items(), key=lambda item: item[1].num, reverse=True)

    try:
        topx = int(sys.argv[2])
    except:
        topx = 10

    for key in mainRecord:
        if topx < 0 : break
        topx -= 1

        method = 'POST' if int(key[1].RequestMethod.POST) > int(key[1].RequestMethod.GET) else "GET"

        # 此处预定
        app0 = key[1].RequestServer.store.get('fr-app', 0)
        app1 = key[1].RequestServer.store.get('fr-app-s1', 0)
        app2 = key[1].RequestServer.store.get('fr-app-s2', 0)

        print key[1], key[0],method,app0, app1,app2


