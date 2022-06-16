#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
将generate_coupons.py生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""
import redis
from generate_coupons import generate_coupons


def save_coupons_to_redis(date):
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)  # 使用连接池
    r = redis.Redis(connection_pool=pool)  # 初始化连接
    date_to_redis = {}  # 初始化数据
    for i in date:
        date_to_redis[i] = 0  # 0 未使用，1 已使用； 默认为未使用
    r.hset('coupons', mapping=date_to_redis)  # hset批量入redis


if __name__ == '__main__':
    date = generate_coupons(200)
    save_coupons_to_redis(date)
