#!/usr/bin/env python
# coding:utf-8
import sys
from redis import Redis
import time


class redisServer(Redis):
    def __init__(self, host, port, db, pwd):
        Redis.__init__(self,
                       host=host,
                       port=port,
                       db=db,
                       password=pwd
                       )

    def __getattr__(self, item):

        if item == 'isWritable':
            timeNow = time.localtime()
            dateNow = time.strftime('%Y-%m-%d %H:%M:%S', timeNow)
            return 1 if self.set('fr-cms-CheckWrite', dateNow, 3600) else 0
        else:
            try:
                return self.info()[item]
            except:
                return False

# shell fr-db:44880 auth item
if __name__ == '__main__':

    from checkList import port_list
    item = port_list[sys.argv[1]]

    redisObj = redisServer(
        host=item[0],
        port=item[1],
        db=15,
        pwd=item[2]
    )

    print getattr(redisObj, sys.argv[2])
