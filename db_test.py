#coding:utf-8
# -*- coding:utf-8 -*-
import pymysql  # 供python3使用

DATABASE = {
            "host": "127.0.0.1",
            "database": "hotel",
            "user": "root",
            "password": "8627139"
        }

# db = pymysql.connect(**DATABASE)
#
# cursor = db.cursor()
# cursor.execute("select id, link from q_list limit 8070,10")
# result = cursor.fetchall()
# print()

# cookies= {}
# with open("q_cookies.txt") as f:
#     text = f.read()
#     cookie = text.replace(" ","").split(";")
#     for c in cookie:
#         key = c.split("=")[0]
#         value = c.split("=")[1]
#         cookies[key] = value
