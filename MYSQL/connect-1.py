#install pymysql first using python -m pip install pymsql in cmd 


import pymysql

conn = pymysql.connect(host="localhost", user="root", password="rps@123",db="demodb_2")

cur=conn.cursor()

cur.execute("select emp_no, first_name, last_name from employee")

records=cur.fetchall()

for rec in records:
    print(rec[0],rec[1],rec[2])  #no of columns

conn.close()

