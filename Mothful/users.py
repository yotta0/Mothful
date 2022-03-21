# Third-party Imports
from werkzeug.security import generate_password_hash
from flask import request, jsonify

# Project Imports
from Mothful import session
from Mothful.models import User

def post_user():
    try:
        username = request.json['username']
        password = request.json['password']
        name = request.json['name']
        email = request.json['email']
        pass_hash = generate_password_hash(password)
        user = User(username, pass_hash, name, email)

        session.add(user)
        session.commit()
        return jsonify({'message': 'User sucessfully register'}), 201
    
    except Exception as e:
        print(e)
        return jsonify({'message': 'Unable to create'}), 500
