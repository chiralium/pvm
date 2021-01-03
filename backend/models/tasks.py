from .mongodb import *


class Tasks(Document):
    id = IntField(primary_key=True)
    uid = StringField(required=True)
    title = StringField(max_length=50)
    deadline_date = StringField(max_length=50)
    deadline_time = StringField(max_length=50)
    time = IntField()
    stamp = IntField()
    priority = IntField()
