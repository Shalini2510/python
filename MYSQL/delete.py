# DELETE A RECORD

import pymysql
import sys
conn = pymysql.connect(host="localhost", user="root", password="rps@123",db="demodb_2")
emp_no=int(input("enter a employee number"))

if not conn:
    sys.exit(0)

try:
    cur=conn.cursor()
    cur.execute(f"delete from employee where emp_no = {emp_no}")
    conn.commit()   #need to be called for action queries
except pymysql.Error as e:
    print(e)

else:
    print("record deleted")
finally:
    conn.close()