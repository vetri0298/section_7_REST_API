import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserResgister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='This field cannot be blank'
        )
    parser.add_argument('password',
        type=str,
        required=True,
        help='This field cannot be blank'
        )

    def post(self):
        data = UserResgister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with that username already exists.'}

        user = UserModel(**data)



        return {'message': 'User has been added successfully.'}, 201
