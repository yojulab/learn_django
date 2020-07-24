from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
client = MongoClient('mongodb://172.17.0.3:27017/')
# db=client.admin
# serverStatusResult=db.command("serverStatus")
# print(serverStatusResult)
mydb = client.mydb
board_info = mydb.board.find()

import pymysql
  
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='tiger', db='yojulabdb',charset='utf8',autocommit=True)
cursor = conn.cursor()
query = "INSERT INTO economic (title,link) VALUES (%s,%s)"
for info in board_info:
    print(type(info), info['title'], info)
    title = info['title']
    link = str(info['likes'])
    cursor.execute(query,(title,link))
conn.commit()
conn.close()
