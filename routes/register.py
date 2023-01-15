from routes.login import *

from app import app, db
from models.models import Users
from werkzeug.security import generate_password_hash
from flask import render_template, request, redirect, url_for
import json


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        login = request.json.get('login')
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        email = request.json.get('email')
        password = request.json.get('password')

        dict = [login, first_name, last_name, email, password]

        if not (first_name or last_name or password or login or email):
            print(login)
        else:
            hashing_password = generate_password_hash(password)
            user = Users(login=login, first_name=first_name, last_name=last_name, email=email,
                         password=hashing_password)

            db.session.add(user)
            db.session.flush()
            db.session.commit()
            print(dict)
            return json.dumps(dict)

    else:
        return render_template('register.html')
