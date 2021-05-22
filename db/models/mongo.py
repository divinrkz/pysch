from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get('DB_URL'))

db = client[os.environ.get('DB_NAME')]

