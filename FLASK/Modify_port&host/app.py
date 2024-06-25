from flask import Flask
#changes need to send values from application to templates:
#1. render the template
#2. import render_template
#3. save the template under the folder named templates
#4. render_template(templatename, variable=value)
#5. SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:{}@localhost:3306/demodb_3".format(quote_plus("rps@123"))
app = Flask(__name__)
@app.route("/")
def hello():
    return "helloworld"

if __name__ == "__main__":
    app.run(port=5500, host="0.0.0.0")
