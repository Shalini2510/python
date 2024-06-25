import pymysql
import sys

import pymysql.cursors
conn = pymysql.connect(host="localhost", user="root", password="rps@123",db="demodb_2", cursorclass=pymysql.cursors.DictCursor)
if not conn:
    sys.exit(0)

try:
    cur=conn.cursor()
    cur.execute("select emp_no, first_name, last_name from employee")
except pymysql.Error as e:
    print(e)

else:
        records=cur.fetchall()
        print(records)
        #for rec in records:
         #   print(f"Number:{rec[0]}, FName:{rec[1]}, LName:{rec[2]}")  #no of columns
finally:
    conn.close()