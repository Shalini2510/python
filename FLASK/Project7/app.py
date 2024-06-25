from flask import Flask ,render_template,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/getValues',methods=['GET','POST'])
def getValues():
    username = request.form['username']  
    email = request.form['email']
    print(username,email)
    return jsonify({'message':"posted succesfully"})

if __name__ == "__main__":
    app.run()
