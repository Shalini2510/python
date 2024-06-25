import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()

def create_app():
    from .models import Product
    app = Flask(__name__,instance_path=os.getcwd(),instance_relative_config=True)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    Migrate(app,db)

    @app.route('/')
    def hello():
        return render_template("index.html")

    @app.route('/addproduct', methods=['GET','POST'])
    def addproduct():
        if request.method == "POST":
            productname = request.json['productname']
            productUnit = request.json['productUnit']
            print(productname,productUnit)
            product = Product(productname=productname,productUnit=productUnit)
            db.session.add(product)
            db.session.commit()
            return jsonify({'message':'Product added successfully'})

    return app