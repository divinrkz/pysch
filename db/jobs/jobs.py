from db.mongo import db
import datetime
from db.enum import EStatus
from db.util import Utility


record = {
    'token': Utility.gen_code(),
    'expiration_date': datetime.datetime.now() + datetime.timedelta(minutes=5),
    'status': EStatus.ACTIVE
}


class Jobs:
    @staticmethod
    def update_token(self, id: str):
        collection = db['tokens']
        # TODO: Custom Exception
        if id is None:
            raise Exception("Id was not given")

        collection.update({'_id': id}, {'$set': {'token': 'This was changed'}})
