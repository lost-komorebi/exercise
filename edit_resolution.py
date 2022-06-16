#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小"""
from PIL import Image
import os

# 图片格式
pic_list = ['.bmp', '.jpg', '.png', '.tif', '.gif', '.pcx', '.tga', '.exif', '.fpx', '.svg', '.psd', '.cdr', '.pcd',
            '.dxf', '.ufo', '.eps', '.ai', '.raw', '.WMF', '.webp', '.avif', '.apng']


def change_size(path, size):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            name, extension = os.path.splitext(filename)  # splitext分开文件名和扩展名

            if extension in pic_list:
                pic_path = os.path.join(dirpath, filename)
                with Image.open(pic_path) as pic:
                    pic.thumbnail(size)  # 图片缩放
                    pic.save(dirpath + name + '_ip5' + extension)  # 加上后缀保存图片


if __name__ == '__main__':
    path = '/Users/komorebi/Desktop/'
    size = 1136, 640  # iphone5分辨率
    change_size(path, size)
