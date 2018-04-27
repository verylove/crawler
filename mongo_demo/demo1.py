#encoding: utf-8

import pymongo

# 获取连接mongodb的对象
client = pymongo.MongoClient("127.0.0.1",port=27017)

# 获取数据库（如果没有zhihu这个数据库，也没有关系）
db = client.zhihu

# 获取数据库中的集合（也就是mysql中的表）
collection = db.qa

# 写入数据
# collection.insert({"username":"aaa"})
# collection.insert_many([
#     {
#         "username":"aaa",
#         'age': 18
#     },
#     {
#         "username":"bbb",
#         'age': 20
#     }
# ])

# 查找数据
# 1. find方法：获取集合中所有的数据
# cursor = collection.find()
# for x in cursor:
#     print(x)

# 2. 获取集合中一条数据
# result = collection.find_one({"age":18})
# print(result)

# 更新数据
# collection.update_one({"username":"bbb"},{"$set":{"username":"ccc"}})
# collection.update_many({"username":"aaa",},{"$set":{"username":"bbb"}})

# 删除数据
# collection.delete_one({"username":"ccc"})
collection.delete_many({"username":"bbb"})