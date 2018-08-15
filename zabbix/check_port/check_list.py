#!/usr/bin/env python
#coding:utf-8
import json,os

port_list = {
    #'redis-cache'   : ['fr-db','44884','aIxdMpfZdHiv7hAb'],
    #'redis-broker'  : ['fr-db','44880','aIxdMpfZdHiv7hAb'],
    'redis-cms':      ['fr-db-s2', '44886','SingCMS$*Ls']
}

value=list()
for key,item in port_list.items():
    print {"{#SERVER}":key,"{#auth}":item.pop(),"{#PORTS}":":".join(item)}
    value.append({"{#SERVER}":key,"{#auth}":item.pop(),"{#PORTS}":":".join(item)})

print value
#print json.dumps({"data":value})
