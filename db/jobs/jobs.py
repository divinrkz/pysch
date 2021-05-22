from db.models.mongo import db
import datetime
from db.models.enum import EStatus
from db.utils.utility import Utility


record = {
    'token': Utility.gen_code(),
    'expiration_date': datetime.datetime.now() + datetime.timedelta(minutes=5),
    'status': EStatus.ACTIVE
}


class Jobs:
    @staticmethod
    def update_instance(_collection: str, _prop: str, _val: str, _dict: dict):
        print('called')
        collection = db[_collection]
        # TODO: Custom Exception
        if id is None:
            raise Exception("Exception Found")

        collection.update({'_id': _prop}, {'$set': {'token': 'This was changed'}})

