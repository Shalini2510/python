#first install flask --> python -m pip install flask
from flask import Flask, render_template

#create an flask instance

app=Flask(__name__)   #__name__ returns current namespace

#flask will by default start at port 5000
#http://127.0.0.1:5000  -/('/' is the top level url of the application)
#create a route for '/'

@app.route('/')
def hello():
    #return "<h1>hello world</h1>"
# to return html page
    #return render_template("hello.html")

#to return mssg
   # message ="this is message from hello()"
    #return render_template("hello.html",msg=message)

#to return list 
    #list_of_names =['alice','bob','pat','alex']
    #return render_template("hello.html",names = list_of_names)

#to return dictionary
    list_of_names =[{'name':'bob'}, {'name':'pat'}, {'name':'alice'}, {'name':'ruby'}]
    return render_template("hello.html",names = list_of_names)
#create a route for '/exampleUrl' 
# run on --> http://127.0.0.1:5000/exampleUrl

@app.route('/exampleUrl')
def example():
   # return "<h1> from example url</h1>"
    return render_template("example.html")

if __name__ == '__main__':
    app.run()  #application will run on port 5000 --> check on browser using http://127.0.0.1:5000

    #stop application by using ctrl+c