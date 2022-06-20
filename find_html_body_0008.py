#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
一个HTML文件，找出里面的正文
"""


from bs4 import BeautifulSoup


def get_html_body(file):
    with open(file, 'r') as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')  # 解析html_doc
        return soup.body.get_text()  # 获取body部分文本


if __name__ == '__main__':
    file = r'./resource/bs4.html'
    get_html_body(file)
    print(get_html_body(file))