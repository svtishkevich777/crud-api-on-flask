from mongoengine import Document, StringField, IntField


class User(Document):
    name = StringField()
    age = IntField()

    meta = {
        'collection': 'user',
        'indexes': [
            'name',
            'age',
        ],
    }
