#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
"""

from collections import Counter
import os


def count_diary_times(file_path, n):
    """
    :param file_path: 文件路径
    :param n: 出现次数前n
    :return:
    """
    result = {}
    for dirpath, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension == '.txt':
                with open(os.path.join(dirpath, filename)) as f:
                    dic = Counter(f.read().split(' '))  # 统计
                    dic_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)  # 将统计结果按单词出现次数降序排列
                    max_words = []  # 取前n出现次数最多的单词
                    for i in range(n):
                        max_words.append(dic_list[i][0])
                    result[filename] = max_words
    return result


if __name__ == '__main__':
    n = 3
    file_path = './resource'
    count_diary_times(file_path, n)
