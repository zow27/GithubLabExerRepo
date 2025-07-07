from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["chinook"]

artist_collection = db['artist']
album_collection = db['album']
track_collection = db['track']

def show_collection(name, collection, limit=5):
    print(f"\n--- {name.upper()} COLLECTION ---")
    for doc in collection.find().limit:
        print(doc)

client.close()