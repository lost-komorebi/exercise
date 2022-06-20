#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
"""
import re

def replace_words(word):
    with open(r'./resource/filtered_words.txt') as f:
        sensitive_words = {}
        for i in f.readlines():
            sensitive_words[i.strip()] = len(i.strip())*'*'
        print(sensitive_words)
        n = 0
        for i in sensitive_words:
            if i in word:
                n += 1
        if n > 0:
            print(re.sub('({})'.format('|'.join(map(re.escape, sensitive_words.keys()))), lambda m: sensitive_words[m.group()], word))
        else:
            print(word)


if __name__ == '__main__':
    word = input("please enter:")
    replace_words(word)
