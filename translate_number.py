#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

def translateNumber(num):
     CHINESE_NEGATIVE = "负"
     CHINESE_ZERO = "零"
     CHINESE_DIGITS = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
     CHINESE_UNITS = ["", "十", "百", "千"]
     CHINESE_GROUP_UNITS = ["", "万", "亿", "兆", "京", "垓", "杼", "穰", "溝", "澗", "正", "載", "極"]

     #数字0
     if num == 0:
        return CHINESE_ZERO

     groupIsZero = True
     needZero = False

     result = ""
     strNum = str(num)
     #负数
     if strNum[0] == "-":
        strNum = strNum[1:]
        result += CHINESE_NEGATIVE

     len1 = len(strNum)
     #从左边开始，循环当前数字的每一位
     for i in range(0, len1):
        #当前数字位所在位置
        position = len1 - 1 - i
        #当前数字位的值
        digit = int(strNum[i])
        #取模，返回余数
        unit = position % len(CHINESE_UNITS)
        #除，返回整数
        group = (position - unit) / len(CHINESE_UNITS)

        if digit != 0:
            if needZero:
                result += CHINESE_ZERO

            if (digit != 1 or unit != 1 or groupIsZero == False or (group == 0 and needZero)):
                result += CHINESE_DIGITS[digit]

            result += CHINESE_UNITS[unit]

        groupIsZero = groupIsZero and (digit == 0)

        if (unit == 0 and groupIsZero == False):
            result += CHINESE_GROUP_UNITS[group]

        needZero = (digit == 0 and (unit != 0 or groupIsZero))

        if unit == 0:
            groupIsZero = True

     return result

# for num in range(-3, 15):
#     print(translateNumber(num))
#
# print(translateNumber(203))