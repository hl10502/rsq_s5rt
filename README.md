## rsq_s5rt

日事清S5跑团打卡统计程序，每周一零点1分定时执行统计跑团成员打卡情况，生成excel文件，并发送Email。
使用Python代码编写。

## 代码结构

* crontab：定时执行的crontab表达式
* date.py：日期、时间工具类
* rsq_request.py：日事清请求URL获取打卡数据
* rsq_s5rt.py：主程序入口,获取打卡数据，生成excel、发送Email
* rsq_s5rt_start.sh：定时执行的sh脚本
* send_email.py：发送Email
* translate_number.py：数字转换成中文汉字
* write_excel.py：使用XlsxWriter操作excel

## 代码分析

请参考 [http://www.hl10502.com/2017/03/29/python-rsq-s5rt/](http://www.hl10502.com/2017/03/29/python-rsq-s5rt/)
