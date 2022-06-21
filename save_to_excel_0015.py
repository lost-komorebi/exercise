#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
请将纯文本文件 city.txt信息写到 student.xls 文件中，如下图所示：
"""
import json
import xlwt

with open('./resource/city.txt') as f:
    city_dic = json.loads(f.read())  # 字符串转为字典
    workbook = xlwt.Workbook()  # 打开Excel
    worksheet = workbook.add_sheet('city')  # 创建sheet
    a = 0
    for x, y in city_dic.items():
        worksheet.write(a, 0, x)  # 写入序号
        worksheet.write(a, 1, y)  # 写入城市
        a += 1
    workbook.save('./resource/city.xls')  # 保存Excel
