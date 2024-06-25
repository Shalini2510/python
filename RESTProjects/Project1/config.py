from urllib.parse import quote_plus
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY="thisisarandomgeneratedstring"
SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:{}@localhost:3306/demodb_3".format(quote_plus("rps@123"))

