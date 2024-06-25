#top level url '/' should render index.html
#from index.html values to be posted to getValues function
import pymysql
from flask import Flask,render_template,request,redirect,url_for
import sys

app=Flask(__name__)
conn= pymysql.connect(host="localhost",user="root",password="rps@123",db="demodb_3")

@app.route('/')
def hello():
    return render_template("index-validation.html")


@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/getValues', methods=['GET','POST'])
def getValues():
    if request.method == 'POST':
        username = request.form['username']
        email =request.form['email']
        password=request.form['password']

        #print(username)
        #print(email)
        #print(password)
        cur=conn.cursor()
        try:
            cur.execute("insert into loginusers(username,email,password)value ('{}','{}','{}')".format(username,email,password))
            conn.commit()
        except pymysql.Error as e:
            print(e, sys.exc_info())
            return "error adding record"

    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run()