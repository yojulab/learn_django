import pymysql
  
conn = pymysql.connect(host='localhost', port=3306, user='scott', passwd='tiger', db='yojulabdb',charset='utf8',autocommit=True)
cursor = conn.cursor(pymysql.cursors.DictCursor)
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print ("Database version : %s " % data)
cursor.execute("SELECT * from economic")
data = cursor.fetchall()
for infor in data:
    print ("economic : %s " % infor['title'])
conn.close()
