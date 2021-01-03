from .mongodb import *
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

class Users(Document):
    id = IntField(primary_key=True, required=True)
    username = StringField(max_length=50, required=True)
    password = StringField(min_length=4, required=True)

class Auth():
    def __init__(self, username, password):
        self.jwt = None
        if username and password:
            user = Users.objects(username=username, password=password)
            if user:
                self.jwt = create_access_token(identity=password)