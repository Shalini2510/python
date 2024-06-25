from flask import Flask ,render_template,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/getValues',methods=['GET','POST'])
def getValues():
    print(request.args)  #to get values in browser link and terminal use 'request.args'
    #username=request.args['username']
    #email=request.args['email']

    #username=request.form['username']  #for post method in index.html we use 'request.form'
    #email=request.form['email']
    #print(username,email)
    return jsonify({'message':"posted succesfully"})

if __name__ == "__main__":
    app.run()
