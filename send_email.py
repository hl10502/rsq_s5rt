#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import date

import logging
LOG = logging.getLogger(__name__)

def send_email(file_name):
    # 第三方 SMTP 服务
    mail_host = "smtp.126.com"  # 设置服务器
    sender = 'xxxx@126.com' #发送者邮箱
    mail_user = "xxxx"  # 发送者用户名
    mail_pass = "yyyy"  # 发送者邮箱密码

    receiver = "zzzz@126.com" #收件者邮箱
    creceiver = "aaaa@qq.com" #抄送这邮箱
    receivers = "zzzz@126.com,aaaa@qq.com" #收件者、抄送这邮箱

    mail_msg = "S5跑团第"+ date.get_curr_week() +"周统计" + date.get_curdate2()
    #如名字所示Multipart就是分多个部分
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message.add_header('Cc', creceiver)
    # 邮箱主题
    message['Subject'] = Header(mail_msg, 'utf-8')

    #xlsx类型附件
    part = MIMEApplication(open(file_name,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=file_name)
    message.attach(part)

    #发送5次，只要发送成功就退出
    for i in range(0, 5):
        try:
            print "邮件发送第" + str(i+1) + "次"
            LOG.debug("邮件发送第" + str(i+1) + "次")
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())  # 发送邮箱、接收邮箱、邮件内容
            smtpObj.close()
            print "邮件发送成功"
            LOG.debug("邮件发送成功")
            break
        except smtplib.SMTPException, e:
            print e
            LOG.error("邮件发送失败：" + str(e))
        except Exception, e1:
            LOG.error("邮件发送失败:" + str(e1))

