from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'myuniqpasswordforflaskapplications'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:flask@mysql/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

with app.app_context():

    from routes.routes import *
    from routes.register import *
    from routes.login import *

    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)

