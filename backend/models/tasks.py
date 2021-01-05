from .mongodb import *


class Tasks(Document):
    N = IntField(required=True)
    uid = StringField(required=True)
    title = StringField(max_length=50)
    deadline_date = StringField(max_length=50)
    deadline_time = StringField(max_length=50)
    time = IntField()
    stamp = IntField()
    priority = IntField()
    newest = BooleanField(max_length=50)
