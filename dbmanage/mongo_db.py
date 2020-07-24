from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
client = MongoClient('mongodb://172.17.0.3:27017/')
# db=client.admin
# serverStatusResult=db.command("serverStatus")
# print(serverStatusResult)
mydb = client.mydb						# get Database	
data = {'title': 'mariaDB 보기', 'tags': ['디비 서비스']}
board_info = mydb.board.insert_one(data)

data = [   
    {"name": "Ram", "age": "26", "city": "Hyderabad"},
    {"name": "Rahim", "age": "27", "city": "Bangalore"}]
res = mydb.board.insert_many(data)
print("Data inserted ......", res.inserted_ids)

data01 = {'tags':{'$regex':'[j]'}}
data02 = {'$push':{'tags':'MySQL02'}}
from bson.objectid import ObjectId
data03 = {'_id': ObjectId('5f1a7063b739d5bc271c53cf')}
res = mydb.board.update_many(data01, data02)
print("Data updateed ......", res.upserted_id)
res = mydb.board.update(data03, data02)
print("Data updateed ......", res)

board_info = mydb.board.find()
for info in board_info:
    if 'title' in info.keys():
        print(type(info), info)
    # print(type(info))
client.close()

# db.board.insert([
# {  title: 'MongoDB Overview', 
#    tags: ['database', 'NoSQL'],
#    likes: 100 },
# {  title: 'MongoDB Overview', 
#    tags: ['mongodb', 'NoSQL'],
#    likes: 10 },
# {  title: 'Neo4j Overview', 
#    tags: ['neo4j', 'database', 'NoSQL'],
#    likes: 750 }])    

