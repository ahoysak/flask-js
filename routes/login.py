from routes.routes import *

from app import app, db
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash
from flask import flash, redirect, request, url_for
import json


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')
        dict_login = [email, password]

        if email and password:

            user = Users.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return json.dumps(dict_login)
            else:
                return redirect(url_for('login'))

    else:
        return render_template('login.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('head_page'))
