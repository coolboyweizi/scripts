#!/usr/bin/env python
# coding:utf-8
import json

port_list = {
    'redis-cache'   : ['fr-db','44884','aIxdMpfZdHiv7hAb'],
    'redis-counter'  : ['fr-db','44880','aIxdMpfZdHiv7hAb'],
    'redis-broker'  : ['fr-db-s2','44885','mobi2017'],
    'redis-cms'     : ['fr-db-s2','44886','SingCMS$*Ls']
}

if __name__ == '__main__':
  value = list()
  for key in port_list:
    value.append({"{#SERVER}": key})
  print json.dumps({"data": value})

