#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

import cookielib
import urllib
import urllib2
import requests

def get_login_session():
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)

    postdata = urllib.urlencode({
        'j_username': 'username', #填写自己的用户名
        'j_password': 'password', #填写自己的密码
        '_spring_security_remember_me': 'true'
    })
    # 登录rishiqing系统的URL
    loginUrl = 'https://www.rishiqing.com/task/j_spring_security_check'

    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    # 模拟登录，并把cookie保存到变量
    result = opener.open(loginUrl, postdata)

    cookie_res = ""
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value
        cookie_res += item.name + "=" + item.value + "; "

    return cookie_res


def get_s5rtdata():
    cookie_res = get_login_session()
    headers = {"Accept": "application/json, text/plain, */*",
           "Content-Type": "application/json;charset=UTF-8",
           "Cookie": cookie_res}

    # 查询S5跑团数据
    r = requests.get("https://www.rishiqing.com/task/v2/kanban/376768?_=1490239997146", headers=headers)
    #print r.status_code
    jsondata = r.json()
    #print jsondata
    #print type(jsondata)
    return jsondata
