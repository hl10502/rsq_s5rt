#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""
import rsq_request
import send_email
import write_excel
import date

import sys
reload(sys)
#设置utf-8编码
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    #获取rishiqing数据
    jsondata = rsq_request.get_s5rtdata()

    file_name = "S5-" + date.get_curdate2() + ".xlsx"

    #生成excel
    write_excel.write_excel(jsondata, file_name)

    #发送email
    send_email.send_email(file_name)
