#!/usr/bin/env python
# -*- coding:utf-8 -*-
# zabbix 主动发现mongodb地址
import json
import subprocess
import psutil
json_data = {"data":[]}

# 获得mongo的监控地址
net_cmd = '''sudo netstat -nlpt|awk '/mongo/{print $4}'
'''
p = subprocess.Popen(net_cmd, shell=True, stdout=subprocess.PIPE)
net_result = p.stdout.readlines()

def get_addr(ip):
  if ip <> '0.0.0.0': return ip
  return psutil.net_if_addrs().get('eth0')[0].address

for server in net_result:
  dic_content = {
      "{#MONGO_PORT}" : server.split(':')[1].strip(),
      "{#MONGO_IPADDR}" : get_addr(server.split(':')[0].strip())
      }
  json_data['data'].append(dic_content)
  result = json.dumps(json_data,sort_keys=True,indent=4)
  print result