#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。
注：只考虑 # ,  \""" 和 \''' 的情况
"""

import os
import re
from functools import reduce


def count_empty_lines(code_list):
    result = {}
    for i in code_list:
        name = os.path.split(i)[1]
        with open(i, 'r') as f:
            empty_lines = sum(1 for line in f if line in ["\n", "\r\n"])  # 统计空格行
            result[name] = {"empty": empty_lines}
    return result


def count_comment_lines(code_list):
    result = {}
    for i in code_list:
        name = os.path.split(i)[1]
        result[name] = {"comment": 0}
        multi_start, multi_end, lineno = 0, 0, 0
        with open(i, 'r') as f:
            for line in f.readlines():
                lineno += 1
                if line.startswith('#') or (line.startswith('"""') and line.endswith('"""')) \
                        or (line.startswith("'''") and line.endswith("'''")):
                    result[name]["comment"] += 1  # 统计单行注释
                if re.match(r'\s+#', line):  # 以至少一个空格开头后面紧跟着'#'
                    result[name]["comment"] += 1  # 统计单行注释
                if line.startswith('"""') and multi_start == 0:
                    multi_start = lineno
                    multi_end = 0
                elif line.startswith('"""') and multi_end == 0 and multi_start != 0:
                    multi_end = lineno
                    result[name]["comment"] += (multi_end - multi_start + 1)  # 统计多行注释
                    multi_start, multi_end = 0, 0  # 置0
    return result


def count_total_lines(code_list):
    result = {}
    for i in code_list:
        name = os.path.split(i)[1]
        with open(i, 'r') as f:
            total_lines = sum(1 for line in f)  # 统计总行数
            result[name] = {"total": total_lines}
    return result


def merge_dict(a, b):
    result = {}
    for x in a:
        for y in b:
            result[x] = {**a[x], **b[y]}  # 使用 **，将两个字典合并
    return result


def run(file_path):
    code_list = []
    for dirpath, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension == '.py':  # 获取所有py文件路径
                code_list.append(os.path.join(dirpath, filename))

    total = count_total_lines(code_list)
    comment = count_comment_lines(code_list)
    empty = count_empty_lines(code_list)

    return reduce(merge_dict, [total, comment, empty])  # 组装结果


if __name__ == '__main__':
    file_path = './'
    run(file_path)
