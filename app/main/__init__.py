from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
#from models import User, BlacklistToken

app = Flask(__name__)
# app.config.from_pyfile('config.py')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:nhucu441@localhost:3306/mydata'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'b\xe1\xfa\xd8h\xa9$\xfax\xad\xb1mS\xb4\x17k\x89'

db = SQLAlchemy(app)
CORS(app)
flask_bcrypt = Bcrypt()

# if __name__ == '__main__':
#     app.run()

def create_app(config_name):
    return app