#INSERT A RECORD

import pymysql
import sys
conn = pymysql.connect(host="localhost", user="root", password="rps@123",db="demodb_2")
if not conn:
    sys.exit(0)

try:
    cur=conn.cursor()
    cur.execute("insert into employee values(10015,'1957-02-12','Alina','George','F','1988-07-11',6900,'d001')")
    conn.commit()   #need to be called for action queries
except pymysql.Error as e:
    print(e)

else:
    print("record added")
finally:
    conn.close()