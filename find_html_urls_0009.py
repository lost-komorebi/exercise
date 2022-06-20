#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
一个HTML文件，找出里面的链接
"""

from bs4 import BeautifulSoup
from urllib.parse import urlparse


def find_html_urls(file):
    with open(file, 'r') as html_doc:
        soup = BeautifulSoup(html_doc, 'html.parser')  # 解析html_doc
        urls = []
        for item in soup.find_all(name='a'):  # 找出所有的a标签
            if 'href' in item.attrs and urlparse(item.get('href')).scheme:  # 如果存在href属性且能解析出URL
                urls.append(item.get('href'))
        return urls


if __name__ == '__main__':
    file = r'./resource/bs4.html'
    find_html_urls(file)
