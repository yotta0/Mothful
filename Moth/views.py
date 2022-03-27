from Mothful import app
from flask import jsonify


@app.route('/scrap', methods=['GET'])
def search():

    return jsonify({'message': 'Running Project'})

