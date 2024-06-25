#UPDATE A ROW BY TAKING empno column name and value as input

import pymysql
import sys
conn = pymysql.connect(host="localhost", user="root", password="rps@123",db="demodb_2")
emp_no=int(input("enter a employee number"))
col_name= input("enter column name")
value=float(input("enter salary"))
if not conn:
    sys.exit(0)

try:
    cur=conn.cursor()
    cur.execute(f"update employee set {col_name} = {value} where emp_no = {emp_no}")
    conn.commit()   #need to be called for action queries
except pymysql.Error as e:
    print(e)

else:
    print("record added")
finally:
    conn.close()