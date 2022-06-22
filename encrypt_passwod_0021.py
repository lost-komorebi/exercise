#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""通常，登陆某个网站或者 APP，需要使用用户名和密码。
密码是如何加密后存储起来的呢？请使用 Python 对密码加密
"""

import hashlib
import string
import random


def get_salt():
    """
    获取随机字符串
    """
    alp = string.ascii_letters
    dig = string.digits
    return ''.join(random.sample(alp + dig, random.randint(10, 20)))


def encrypt_pwd(password, salt):
    """
    先对密码进行sha1加密，在将得到的加密数据和slat一起md5加密
    """
    sha1 = hashlib.sha1()
    sha1.update(password.encode('utf-8'))
    md5 = hashlib.sha1()
    md5.update(sha1.hexdigest().encode('utf-8'))
    md5.update(salt.encode('utf-8'))
    return md5.hexdigest()


if __name__ == '__main__':
    salt = get_salt()
    password = 'abc'
    encrypt_pwd(password, salt)
