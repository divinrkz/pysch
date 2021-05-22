from .mongo import collection
import datetime
from .enum import EStatus
from .util import Utility

record = {
    'token': Utility.gen_code(),
    'expiration_date': datetime.datetime.now() + datetime.timedelta(minutes=5),
    'status': EStatus.ACTIVE
}

instance = collection.insert(record)]

class Job:
    def __str__(self):
        col = collection

    def update_token(self, id: str):
        if id is None:

