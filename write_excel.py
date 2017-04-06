#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

import xlsxwriter
import re

import date
import translate_number

def write_excel(jsondata, file_name):
    #获取当前时间在年度内的第几个星期
    currweek = date.get_curr_week()
    currweek_num = int(currweek)
    #currweek_num = 14
    col_num = currweek_num + 2

    s5ptname = jsondata['name']
    kanbanCardList = jsondata['kanbanCardList']

    workbook = xlsxwriter.Workbook(file_name) # 创建一个excel文件
    worksheet = workbook.add_worksheet(s5ptname) # 创建一个excel文件的工作表 括号为空就是默认名

    # add_format() 为当前workbook添加一个样式名为titleformat
    titleformat = workbook.add_format()
    titleformat.set_bold() # 设置粗体字
    titleformat.set_font_size(10) # 设置字体大小为10
    titleformat.set_font_name('Microsoft yahei') # 设置字体样式为雅黑
    titleformat.set_align('center') # 设置水平居中对齐
    titleformat.set_align('vcenter') # 设置垂直居中对齐
    # 将titleformat应用在第一行，此行为标题
    worksheet.set_row(0, None, titleformat)

    #加粗、红色字体、自动换行
    format = workbook.add_format({'bold': True, 'font_color': 'red', 'text_wrap': True})

    worksheet.write('A1', s5ptname + '成员')
    worksheet.set_column('A:A', 14) #定义A列宽度为20

    #只创建5-6列
    #num = 5
    #从第2周开始创建全部
    num = currweek_num - 2
    j = 0
    #dictA = {}
    dictB = {}

    safflower_col = ""
    safflower_num_col = ""

    #从字母b开始
    for i in range(98, 123):
        chr_str = chr(i).upper()
        if num > 0:
            week_name = "第" + str(currweek_num - num) + "周"
        elif num == 0:
            week_name = '小红花✿'
            safflower_col = chr_str
            worksheet.set_column(chr_str + ':'+ chr_str, 20) #定义列宽度为20
        elif num == -1:
            week_name = '小红花总计'
            safflower_num_col = chr_str
        else:
            break
        worksheet.write(chr_str + '1', week_name)
        #dictA.setdefault(chr_str, week_name)
        dictB.setdefault(week_name, chr_str)
        num -= 1

    if col_num > 26:
        #从字母a开始
        for i in range(97, 123):
            chr_str = "A" + chr(i).upper()
            if num > 0:
                week_name = "第" + str(currweek_num - num) + "周"
            elif num == 0:
                week_name = '小红花✿'
                safflower_col = chr_str
                worksheet.set_column(chr_str + ':'+ chr_str, 20) #定义列宽度为20
            elif num == -1:
                week_name = '小红花总计'
                safflower_num_col = chr_str
            else:
                break
            worksheet.write(chr_str + '1', week_name)
            #dictA.setdefault(chr_str, week_name)
            dictB.setdefault(week_name, chr_str)
            num -= 1

    if col_num > 52:
        #从字母a开始
        for i in range(97, 123):
            chr_str = "B" + chr(i).upper()
            if num > 0:
                week_name = "第" + str(currweek_num - num) + "周"
            elif num == 0:
                week_name = '小红花✿'
                safflower_col = chr_str
                worksheet.set_column(chr_str + ':'+ chr_str, 20) #定义列宽度为20
            elif num == -1:
                week_name = '小红花总计'
                safflower_num_col = chr_str
            else:
                break
            worksheet.write(chr_str + '1', week_name)
            #dictA.setdefault(chr_str, week_name)
            dictB.setdefault(week_name, chr_str)
            num -= 1

    row_num = 2
    for kanbanCard in kanbanCardList:
        worksheet.write('A' + str(row_num), kanbanCard['name'])

        safflower_num = 0
        safflower_label = ""

        kanbanItemList = kanbanCard['kanbanItemList']
        for kanbanItem in kanbanItemList:
            week_plan = kanbanItem['name']

            #正则表达式匹配'周'前面的数字
            SEARCH_PAT = re.compile(r'(\d+)\s*' + u'周') #汉字先转换成unicode
            pat_search = SEARCH_PAT.search(week_plan)
            if pat_search != None:
                week_plan = pat_search.group(1)
            else:
                #正则表达式匹配'W'后面的数字
                SEARCH_PAT = re.compile(r'W\s*(\d+)')
                pat_search = SEARCH_PAT.search(week_plan)
                if pat_search != None:
                    week_plan = pat_search.group(1)

            #从第2周开始，到当前周
            for i in range(2, currweek_num):
                #数字转换成中文汉字
                cnnum = translate_number.translateNumber(i)
                week_cnnum = '第'+ str(i) + '周'
                col = dictB.get(week_cnnum)

                # 汉字前需要加'u'转换成Unicode
                if week_plan == str(i) or week_plan.find(u"第" + cnnum + u"周") != -1:
                    #有周计划（建卡），小红花加1
                    safflower_num += 1
                    safflower_label += "✿"

                    isDone = kanbanItem['isDone']
                    value = ""
                    if isDone:
                        #value = '✓'
                        value = '✓✿✿'
                        #有完成周计划（打卡），小红花加1
                        safflower_num += 1
                        safflower_label += "✿"

                        # 第2周打卡奖励4个小红花
                        if i == 2:
                            safflower_num += 4
                            safflower_label += "✿✿✿✿"
                            value += '✿✿✿✿'
                    else:
                        #value = '未打卡'
                        value = '?✿'

                        # 第2周建卡未打卡奖励2个小红花
                        if i == 2:
                            safflower_num += 2
                            safflower_label += "✿✿"
                            value += '✿✿'
                    if col:
                        worksheet.write(col + str(row_num), value, format)

                    #找到当前周，退出循环
                    break

            #小红花
            worksheet.write(safflower_col + str(row_num), safflower_label, format)
            worksheet.write(safflower_num_col + str(row_num), safflower_num, format)

        row_num += 1

    workbook.close()
