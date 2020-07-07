from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help = "This field must not be blank."
    )

    parser.add_argument('store_id',
    type=int,
    required=True,
    help = "Every item needs a store id."
    )

    @jwt_required()
    def get(self, name): # get will look into that list of items and give the specified one
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'No item found on that name'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': f'An item with name {name} already exists.'}, 400 #400 means bad request

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured inserting the item.'}, 500 #Internal server error

        return item.json(), 201 #201 is for mentioning the object has been created.

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item has been deleted.'}

    def put(self, name):

        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
