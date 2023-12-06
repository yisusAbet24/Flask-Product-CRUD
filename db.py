from pymongo import MongoClient
import certifi

MONGO_URI = ""
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["products_app"]
    except ConnectionError:
        print('Database connection error')
    return db