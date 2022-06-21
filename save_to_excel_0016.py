#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
请将纯文本文件 numbers.txt信息写到 student.xls 文件中，如下图所示：
"""
import json
import xlwt

with open('./resource/numbers.txt') as f:
    num_dic = json.loads(f.read())  # 字符串转为字典
    workbook = xlwt.Workbook()  # 打开Excel
    worksheet = workbook.add_sheet('numbers')  # 创建sheet
    a, b = 0, 0
    for x in num_dic:
        for y in x:
            worksheet.write(a, b, y)  # 写入
            b += 1
        a += 1
        b = 0
    workbook.save('./resource/numbers.xls')  # 保存Excel
