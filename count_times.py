#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
任一个英文的纯文本文件，统计其中的单词出现的个数
"""
from collections import Counter

def count_times(file):
    with open(file, 'r') as f:
        text = f.read().split(' ')
        text = [i for i in text if i.isalpha()]
        return Counter(text)


if __name__ == '__main__':
    file = 'article.txt'
    count_times(file)
