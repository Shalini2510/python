from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')

def index():
    return "index method"

@app.route('/hello')
def hello():
    #list_of_names =['alice','bob','pat','alex']
    list_of_names =[
        {'name':'bob', 'age':24},
        {'name':'pat', 'age':14},
        {'name':'alex', 'age':13},

    ]
    return render_template("hello.html",names = list_of_names)

if __name__ == '__main__':
    app.run() 