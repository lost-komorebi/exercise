#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""用 Python 写一个爬图片的程序，从百度贴吧爬图片"""

import requests
from bs4 import BeautifulSoup
import threading


def get_pic_url(soup):
    """获取html中的所有图片URL"""
    urls = []
    for item in soup.find_all(name='img',
                              attrs={"class": "BDE_Image"}):  # 查找标签名为im，且class属性=BDE_Image数据
        urls.append(item.get("src"))
    return urls


def check_next_page(soup):
    """检查是否存在下一页"""
    for item in soup.find_all(name='a'):
        if item.text == '下一页':
            return item.get('href')


def save_pic(url, path):
    r = requests.get(url, stream=True)
    pic_name = url.split('?')[0].split('/')[-1]  # 从URL获取图片名称
    full_path = path + pic_name
    with open(full_path, 'wb') as f:  # 保存图片
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)


def get_soup(url):
    """获取URL的BeautifulSoup对象"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def run(todo_url, path):
    soup = get_soup(todo_url)
    url_list = []
    while check_next_page(soup):
        pn = check_next_page(soup).split('=')[1]  # 获取下一页页码
        next_url = todo_url + '?pn=' + pn  # 组装下一页URL
        soup = get_soup(next_url)
        url_list += get_pic_url(soup)
    for url in url_list:
        t = threading.Thread(target=save_pic(url, path),  # 使用多线程爬取图片
                             name='LoopThread')
        t.start()


if __name__ == '__main__':
    todo_url = 'https://tieba.baidu.com/p/6765369539'
    path = './resource/BDE_Image/'
    run(todo_url, path)
