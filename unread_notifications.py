"""
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果
"""
from PIL import Image, ImageDraw, ImageFont
from random import randint

with Image.open('WeChat.jpeg') as pic:
    print(pic.format, pic.size, pic.mode)

    img_draw = ImageDraw.Draw(pic)  # 创建draw对象
    ttf = 'FZZJ-ZYGDKJW-2.ttf'  # 字体文件
    font = ImageFont.truetype(font=ttf, size=50)  # 设置使用的字体的文件以及字体大小
    n = str(randint(1, 10))  # 生成一个随机消息数
    img_draw.text((pic.size[0] - font.size, 0), n, font=font,
                  fill=(255, 0, 0))  # 在图片上写字，第一个参数为位置，第二个参数为要写的文字，第三个参数为字体，最后一个为字体的颜色
    pic.show() # 显示图片
