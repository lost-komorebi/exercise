#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

"""
将generate_coupons.py生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
"""
from generate_coupons import generate_coupons
import mysql.connector


def save_to_database(data):
    """
    mysql version:8.0.29
    """
    mysql_insert_query = 'insert into coupons(coupon)VALUES (%s)'  # insert sql
    records_to_insert = []  # 组装待入库数据
    for i in data:
        records_to_insert.append((str(i),))  # 注意要以tuple方式入库

    conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', port='3306', database='test',
                                   auth_plugin='mysql_native_password')  # 连接mysql
    cursor = conn.cursor()  # 创建游标
    cursor.execute(
        'drop table if exists `coupons`;')
    cursor.execute(
        'CREATE TABLE `coupons`( `id` int(10) unsigned NOT NULL AUTO_INCREMENT, `coupon` varchar(10) NOT NULL, PRIMARY KEY (`id`), UNIQUE KEY `unique_coupon` (`coupon`) USING BTREE) ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    )  # 建表
    conn.commit()  # 提交
    cursor.executemany(
        mysql_insert_query, records_to_insert)  # 执行入库sql
    conn.commit()  # 提交
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接


if __name__ == '__main__':
    data = generate_coupons(200)
    save_to_database(data)
