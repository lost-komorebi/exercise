#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
"""将 第 0014 题中的 student.xls 文件中的内容写到 student.xml  文件
https://docs.python.org/zh-cn/3/library/xml.dom.minidom.html#module-xml.dom.minidom
"""

import xlrd
from lxml import etree
from pprint import pformat


def get_data():
    workbook = xlrd.open_workbook('./resource/student.xls')  # 打开xls
    sheet = workbook.sheets()[0]  # 获取第一个sheet

    rows, cols = sheet.nrows, sheet.ncols  # 获取行数，列数
    stu_dic = {}  # 组装数据
    for x in range(rows):
        stu_dic[sheet.cell(x, 0).value] = []
        for y in range(1, cols):
            v = sheet.cell(x, y).value
            stu_dic[sheet.cell(x, 0).value].append(int(v) if type(v) == float else v)
    return stu_dic


def write_xml(data):
    root = etree.Element("root")  # 构建根结点
    students = etree.SubElement(root, 'students')  # 将students节点添加到root节点下
    students.text = '\n'  # 为students节点添加文本内容
    comment = etree.Comment('\n 学生信息表\n"id" : [名字, 数学, 语文, 英文]\n')  # 注释
    comment.tail = '\n' + pformat(data, width=35) + '\n'
    students.append(comment)  # students节点添加注释
    etree.ElementTree(root).write('./resource/student.xml', pretty_print=True,
                                  encoding='utf-8', xml_declaration=True)  # 写入xml文件


if __name__ == '__main__':
    data = get_data()
    write_xml(data)
