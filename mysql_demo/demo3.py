#encoding: utf-8

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='root',database='pymysql_demo',port=3306)
cursor = conn.cursor()

# select username,age from user where id=1
# select * from user
# select id,username,age,password from user

# sql = """
# select username,age from user where id=2
# """

######## fetchone ########
# sql = """
# select * from user
# """
# cursor.execute(sql)
# while True:
#     result = cursor.fetchone()
#     if result:
#         print(result)
#     else:
#         break
#
# conn.close()

######## fetchall ########
# sql = """
# select * from user
# """
# cursor.execute(sql)
# results = cursor.fetchall()
# for result in results:
#     print(result)
# conn.close()

######## fetchmany ########
sql = """
select * from user
"""
cursor.execute(sql)
results = cursor.fetchmany(3)
for result in results:
    print(result)
conn.close()