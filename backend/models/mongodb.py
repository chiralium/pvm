from mongoengine import *
import os

connect(
    os.environ.get('MONGO_DB'),
    host='mongo',
    username=os.environ.get('MONGO_U'),
    password=os.environ.get('MONGO_P'),
    authentication_source=os.environ.get('MONGO_DB')
)
