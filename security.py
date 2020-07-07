
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)    #if there is no mentioned username it will return None
    if user and user.password == password:
        return user

def identity(payload): #payload is the contents of JWT
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
