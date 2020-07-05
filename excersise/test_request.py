#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 11:03
# @Author  : datan
# @Site    : 


# #封装一个http请求
import requests
def http_request(url,data,method,token=None):
    header = {"X-Lemonban-Media-Type": "lemonban.v2", 'Authorization': token}
    if method.upper()=="POST":
        response= requests.post(url, json=data, headers=header)
        return response
    elif method.upper()=='GET':
        response= requests.get(url, params=data, headers=header)
        return response
