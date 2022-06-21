#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml   文件
"""

import xlrd
from lxml import etree
from pprint import pformat


def get_data():
    workbook = xlrd.open_workbook('./resource/numbers.xls')  # 打开xls
    sheet = workbook.sheets()[0]  # 获取第一个sheet

    rows, cols = sheet.nrows, sheet.ncols  # 获取行数，列数
    num_dic = []  # 组装数据
    for x in range(rows):
        num_dic.append([])
        for y in range(0, cols):
            v = int(sheet.cell(x, y).value)
            num_dic[x].append(v)
    return num_dic


def write_xml(data):
    root = etree.Element("root")  # 构建根结点
    numbers = etree.SubElement(root, 'numbers')  # 将numbers节点添加到root节点下
    numbers.text = '\n'  # 为numbers节点添加文本内容
    comment = etree.Comment('\n 数字信息\n')  # 注释
    comment.tail = '\n' + pformat(data, width=20) + '\n'
    numbers.append(comment)  # numbers节点添加注释
    etree.ElementTree(root).write('./resource/number.xml', pretty_print=True,
                                  encoding='utf-8', xml_declaration=True)  # 写入xml文件


if __name__ == '__main__':
    data = get_data()
    write_xml(data)
