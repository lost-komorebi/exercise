#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""将 第 0015 题中的 city.xls 文件中的内容写到 city.xml  文件
"""

import xlrd
from lxml import etree
from pprint import pformat


def get_data():
    workbook = xlrd.open_workbook('./resource/city.xls')  # 打开xls
    sheet = workbook.sheets()[0]  # 获取第一个sheet

    rows, cols = sheet.nrows, sheet.ncols  # 获取行数，列数
    city_dic = {}  # 组装数据
    for x in range(rows):

        for y in range(1, cols):
            v = sheet.cell(x, y).value
            city_dic[sheet.cell(x, 0).value] = v
    return city_dic


def write_xml(data):
    root = etree.Element("root")  # 构建根结点
    cities = etree.SubElement(root, 'cities')  # 将cities节点添加到root节点下
    cities.text = '\n'  # 为cities节点添加文本内容
    comment = etree.Comment('\n 城市信息\n')  # 注释
    comment.tail = '\n' + pformat(data, width=20) + '\n'
    cities.append(comment)  # cities节点添加注释
    etree.ElementTree(root).write('./resource/city.xml', pretty_print=True,
                                  encoding='utf-8', xml_declaration=True)  # 写入xml文件


if __name__ == '__main__':
    data = get_data()
    write_xml(data)
