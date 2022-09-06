from pymongo import MongoClient


uri = "mongodb://vagrant:vagrant@localhost:27017/admin"


def connect_to_mongo_db(data):
    # Replace the uri string with your MongoDB deployment's connection string.
    client = MongoClient(uri)

    # database and collection code goes here
    db = client.admin
    coll = db.papers

    # drop current entries from database
    coll.drop() 
    # insert code goes here
    result = coll.insert_many(data)
    # display the results of your operation
    print(result.inserted_ids)
    # Close the connection to MongoDB when you're done.
    client.close()
