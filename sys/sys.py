#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !/usr/bin/env python
# coding:UTF-8
import MySQLdb

try:
    conn = MySQLdb.connect(host="localhost", user='root', passwd='123', db='test')
    cursor = conn.cursor()  # 创建一个游标对象
    sql = "select * from user"
    cursor.execute(sql)  # 执行一个sql（游标对象操作）
    for i in cursor.fetchall():  # 列出执行的结果
        print
        i
    conn.commit()  # 事务提交（对数据库修改必须使用这个方法，否则数据不会被真正写入）
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接
exceptException, e:
print
"connection error:" + str(e)