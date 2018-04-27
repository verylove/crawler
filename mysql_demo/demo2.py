#encoding: utf-8

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='root',database='pymysql_demo',port=3306)

cursor = conn.cursor()

# insert into user(id,username,age,password) values(2,'bbb',20,'111111')
# sql = """
# insert into user(id,username,age,password) values(2,'bbb',20,'111111')
# """
# cursor.execute(sql)
# conn.commit()


sql = """
insert into user(id,username,age,password) values(null,%s,%s,%s)
"""

username = 'spider'
age = 21
password = '12345'

cursor.execute(sql,(username,age,password))
conn.commit()


conn.close()