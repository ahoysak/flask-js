from models.models import *

from app import app, db
from flask import render_template


@app.route('/')
def head_page():
    users = Users.query.all()
    return render_template('index.html', users=users)







