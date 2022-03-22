from Mothful import app, users
from flask import jsonify


@app.route('/', methods=['GET'])
def root():
    return jsonify({'message': 'Running Project'})


@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user()

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return users.get_user(id)

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    return users.update_user(id)

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    return users.delete_user(id)
