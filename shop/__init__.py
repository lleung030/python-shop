from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# # create the extension
# db = SQLAlchemy()
# # create the app
# app = Flask(__name__)
# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myshop.db"
# # initialize the app with the extension
# db.init_app(app)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///myshop.db'
app.config['SECRET_KEY'] = 'ouehdvouiqernhhvoweirn'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.admin import routes