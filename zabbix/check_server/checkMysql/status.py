#!/usr/bin/env python
# coding:utf-8
import pymysql
import sys

class Mysql():

    _status_by_host_items = (
        'Bytes_received', 'Bytes_sent', 'Questions','Slow_queries'
    )

    def __init__(self, host='localhost', user='root', password='', port=3306):
        self.host = host
        self.user = user

        self.connect = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )
        self.cursor = self.connect.cursor()

    # 查询performance_schema数据
    def _performance(self, field, table, condition="1=1"):
        sql = "SELECT %s FROM performance_schema.%s WHERE %s " \
              % (field, table, condition)
        return self.cursor.execute(sql)


    # 获取status_by_host表
    def _status_by_host(self, VARIABLE_NAME):
        condition = (
            "`VARIABLE_NAME`='%s'" %( VARIABLE_NAME),
            "`host`= '%s'" % ( self.host)
        )
        self._performance('`VARIABLE_VALUE`', 'status_by_host', ' AND '.join(condition))

    # 检查数据库可写。写入test
    def _checkWrite(self):
        import time
        sql = "INSERT test.checked values (0,%d)" %(int(time.time()))
        self.cursor.execute(sql)
        self.connect.commit()

    # 获取属性
    def __getattr__(self, item):
        if item == 'write':
            self._checkWrite()
            data = self.cursor.lastrowid
            self.cursor.close()
            self.connect.close()
            return data
        else:
            self.host = sys.argv[-2]
            if item in self._status_by_host_items:
                self._status_by_host(item)
                data = self.cursor.fetchone()
                self.cursor.close()
                self.connect.close()
                return data[0]
            else:
              return None

if __name__ == '__main__':
   if sys.argv[-1] == "write":
        c = Mysql(
            host=sys.argv[1].split(':')[0],
            user=sys.argv[2],
            password=sys.argv[3],
            port=int(sys.argv[1].split(':')[1])
        )
        print getattr(c,'write')

   else:
       c = Mysql()
       print getattr(c,sys.argv[-1])

