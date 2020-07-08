from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#since we are using falsk_restful we no longer need jsonify while returning stuffs.
from security import authenticate, identity
from resources.user import UserResgister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXEPTIONS'] = True
api = Api(app)
app.secret_key = 'Kane'


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/chair
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserResgister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) # this debug TRUE will give us a detailed HTML page whenever the error occurs in the application
