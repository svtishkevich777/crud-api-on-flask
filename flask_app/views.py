from flask import jsonify, request
from mongoengine.errors import ValidationError

from flask_app.connectdb import app
from flask_app.models import User


@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify({'message': 'Validation Error', 'errors': error.to_dict()})
    response.status_code = 400
    return response


@app.route('/', methods=['GET'])
def home():
    return '''
    <html>
        <head>
            <style>
                h1 {text-align: center;}
                p {text-align: center;}
            </style>
        </head>
        <body>
            <h1>Home Page Flask</h1>
            <p><a href="http://0.0.0.0:8080/api/v1/users">/api/v1/users</a></p>
        </body>
    </html>'''


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], age=data['age'])
        new_user.save()
    except ValidationError as e:
        return jsonify({'message': 'BAD REQUEST', 'errors': e.to_dict()}), 400

    return jsonify({'message': 'User created successfully', 'user_id': str(new_user.id)}), 201


@app.route('/api/v1/users', methods=['GET'])
def get_all_users():

    returned_users = User.objects.all().to_json(indent=2)

    return returned_users, 200


@app.route('/api/v1/users/<pk>', methods=['GET'])
def get_user(pk):
    try:
        user = User.objects.get(id=pk).to_json(indent=2)
        return user, 200
    except User.DoesNotExist:
        return jsonify({'message': 'User does not exist'}), 404


@app.route('/api/v1/users/<pk>', methods=['PUT'])
def update_user(pk):
    data = request.get_json()
    count = User.objects.filter(id=pk).update(**data)
    if count:
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User does not exist'}), 204

@app.route('/api/v1/users/<pk>', methods=['DELETE'])
def delete_user(pk):
    count = User.objects.filter(id=pk).delete()
    if count:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User does not exist'}), 204
