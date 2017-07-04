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

import logging
BASE_FORMAT = "[%(name)s][%(levelname)-6s] %(message)s"
FILE_FORMAT = "[%(asctime)s]" + BASE_FORMAT

LOG = logging.getLogger(__name__)


# 设置日志
def setlog():
    # root_logger日志
    root_logger = logging.getLogger()
    # 设置root_logger日志级别为DEBUG
    root_logger.setLevel(logging.DEBUG)

    # 控制台日志
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FILE_FORMAT))
    # 设置日志级别为WARNING
    sh.setLevel(logging.WARNING)
    root_logger.addHandler(sh)

    # 文件日志
    fh = logging.FileHandler('rsq_s5rt-{0}.log'.format(date.get_curdate2()))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter(FILE_FORMAT))
    # 将 fh添加到root_logger
    root_logger.addHandler(fh)

if __name__ == '__main__':

    try :
        #设置日志
        setlog()

        #获取rishiqing数据
        LOG.debug("开始获取日事清数据")
        jsondata = rsq_request.get_s5rtdata()

        file_name = "S5-" + date.get_curdate2() + ".xlsx"
        LOG.debug("xlsx文件名称为：" + file_name)
        #生成excel
        write_excel.write_excel(jsondata, file_name)
        LOG.debug("数据已写入xlsx文件：" + file_name)

        #发送email
        LOG.debug("开始发送Email" )
        send_email.send_email(file_name)

    except Exception, e:
        LOG.error(e.message)
        raise



