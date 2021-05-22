from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

succotash_db = client['succotash_db']

tokens_collection = succotash_db['tokens']


instance = {
    token: 'MongoDB and Python',
    description: 'MongoDB is no SQL database',
    tags: ['mongodb', 'database', 'NoSQL'],
    viewers: 104
}

# inserting the data in the database
rec = mydatabase.myTable.insert(record)