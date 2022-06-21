#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
请将纯文本文件 student.txt为学生信息写到 student.xls 文件中，如下图所示：
"""
import json
import xlwt

with open('./resource/student.txt') as f:
    stu_dic = json.loads(f.read())  # 字符串转为字典
    workbook = xlwt.Workbook()  # 打开Excel
    worksheet = workbook.add_sheet('sheet1')  # 创建sheet
    a, b = 0, 0
    for x in stu_dic:
        worksheet.write(a, 0, x)  # 写入序号
        b = 1
        for y in stu_dic[x]:
            worksheet.write(a, b, y)  # 写入学生名称和分数
            b += 1
        a += 1

    workbook.save('./resource/student.xls')
