#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）
"""
import shortuuid


def generate_coupons(n):
    coupons = []
    for i in range(n):
        coupon = shortuuid.ShortUUID().random(length=10)
        coupons.append(coupon)
    return coupons


if __name__ == '__main__':
    generate_coupons(200)
