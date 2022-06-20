#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""使用 Python 生成类似于下图中的字母验证码图片
1.用随机颜色填充背景
2.生成字母
3.对图片进行模糊处理
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
from random import sample, randint


def random_bg_color():
    """
    获取随机像素值，填充背景
    """
    return (randint(97, 255), randint(97, 255), randint(97, 255))


def random_str_color():
    """
    获取随机像素值，作为字体颜色，注：与背景填充色错开
    """
    return (randint(32, 50), randint(32, 50), randint(32, 50))


def draw_code_pic():
    alp = string.ascii_uppercase * 2  # 使验证码可以出现重复字母
    code_str = ''.join(sample(alp, 4))  # 随机4位字母
    size = (150, 50)
    color = (255, 255, 255)
    pic = Image.new('RGB', size, color)  # 创建一张白底图片
    ttf = 'FZZJ-ZYGDKJW-2.ttf'  # 字体文件
    font = ImageFont.truetype(font=ttf, size=50)  # 字体文件或字体对象中读取字体并返回一个字体对象
    d = ImageDraw.Draw(pic)  # 创建draw对象

    # 填充背景
    for x in range(size[0]):
        for y in range(size[1]):
            if randint(0, 100) > 50:  # 绘制点的概率
                d.point((x, y), fill=(randint(32, 96), randint(32, 96), randint(32, 96)))  # 在指定坐标绘制点

    d.text((5, 3), code_str, font=font, fill=random_str_color())  # 在图片上写字，第一个参数为位置，第二个参数为要写的文字，第三个参数为字体，最后一个为字体的颜色
    pic = pic.filter(ImageFilter.BLUR)  # 对图片进行模糊处理
    pic.show()  # 显示图片


if __name__ == '__main__':
    draw_code_pic()
