#!/usr/bin/python
# -*- coding:utf-8 -*-
# author:b1ng0

import requests
import threading 
import random

maxs=100  ##并发的线程数量
threadLimiter=threading.BoundedSemaphore(maxs)

class GetVaildIp(threading.Thread):

    def __init__(self, proxy):
        super().__init__()
        self._proxy = proxy
    
    def run(self):
        threadLimiter.acquire()  #获取
        try:
            proxy_url = 'http://{}:{}'.format(self._proxy['ip'], self._proxy['port'])
            resp = requests.get('http://api.ipify.org', 
            proxies={'http': proxy_url},
            timeout=5)
            if resp.status_code == 200:
                print(proxy_url)
        except:
            pass
        finally:
            threadLimiter.release() #释放


json_resp = requests.get('http://47.101.217.127:8899/api/v1/proxies?limit=100').json()

for proxy in json_resp['proxies']:
    cur = GetVaildIp(proxy)
    cur.start()

for proxy in json_resp['proxies']:
    cur.join()


