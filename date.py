#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 时间、日期
Desc : 
"""

import time
def get_curdate():
    curdate = (time.strftime('%Y-%m-%d', time.localtime(time.time())))
    return curdate

def get_curdate2():
    curdate = (time.strftime('%Y%m%d', time.localtime(time.time())))
    return curdate

def get_curr_week():
    #获取当前时间在年度内的第几个星期
    currweek = time.strftime("%W")
    #currweek_num = int(currweek)
    return currweek