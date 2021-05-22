from .mongo import collection
import datetime
from .enum import EStatus
from .util import Util

record = {
    'token': Util.gen_code(),
    'expiration_date': datetime.datetime.now() + datetime.timedelta(minutes=5),
    'status': EStatus.ACTIVE
}

print(record)

instance = collection.insert(record)
