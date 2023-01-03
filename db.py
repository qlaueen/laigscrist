from flask_pymongo import pymongo
from dotenv import dotenv_values
import os

def get_listings_collection():
    config = dotenv_values(".env")
    DATABASE_URL = f'mongodb+srv://qlaueen:{os.environ.get("password")}@laigscrist.wbkqxu7.mongodb.net/?retryWrites=true&w=majority'
    try:
        client = pymongo.MongoClient(DATABASE_URL)
        db = client.get_database('laigscrist')
        return pymongo.collection.Collection(db, 'listings')
    except pymongo.errors.ConnectionFailure as e:
        print("MongoDB server connection error.")
    except Exception as e:
        print(e)

listings_collection = get_listings_collection()
