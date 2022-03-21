from Mothful import app, users
from flask import jsonify


@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Running Project'})


@app.route('/users', methods=['POST'])
def login():
    return users.post_user()
