# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test.py  
   Description :  
   Author :       JHao
   date：          2017/3/7
-------------------------------------------------
   Change Activity:
                   2017/3/7: 
-------------------------------------------------
"""
__author__ = 'JHao'

import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content


proxy = get_proxy()
print(proxy)