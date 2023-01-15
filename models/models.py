from app import app, manager, db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    login = db.Column(db.String(250), nullable=False, unique=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)


@manager.user_loader
def load_user(id_user):
    return Users.query.get(id_user)

