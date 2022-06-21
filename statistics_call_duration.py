#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""
 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，
 然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
 就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
"""

import xlrd
import re


def format_time(seconds):
    time_format = '{}小时{}分{}秒'.format(seconds // 3600,
                                      (seconds % 3600) // 60,
                                      seconds % 60)
    return time_format


def get_data(file):
    workbook = xlrd.open_workbook(file)  # 打开xls
    sheets = workbook.sheets()  # 获取所有sheet
    res = {}
    for sheet in sheets:
        rows = sheet.nrows  # 获取行数
        total_seconds = 0
        for x in range(1, rows):
            v = sheet.cell(x, 3).value
            if '分' in v:  # 当通话时长不足1分钟时，excel中只会显示秒数，比如'30秒'
                minutes = int(re.split('分|秒', v)[0])
                seconds = int(re.split('分|秒', v)[1])
                time = minutes * 60 + seconds
                total_seconds += time
            else:
                seconds = int(re.split('分|秒', v)[0])
                total_seconds += seconds
        res[sheet.name] = format_time(total_seconds)
    return res


if __name__ == '__main__':
    file = './resource/2022年01-04月语音通信.xls'
    get_data(file)
