#encoding: utf-8

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='root',database='pymysql_demo',port=3306)
cursor = conn.cursor()

# sql = """
# delete from user where id=1
# """
# cursor.execute(sql)
# # 插入、删除、更新。
# # 都需要执行commit操作
# conn.commit()

sql = """
update user set username='bbb'
"""
cursor.execute(sql)
# 插入、删除、更新。
# 都需要执行commit操作
conn.commit()


conn.close()