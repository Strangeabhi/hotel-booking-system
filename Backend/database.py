from flask_pymongo import PyMongo

mongo = None

def init_db(app):
    global mongo
    app.config["MONGO_URI"] = "mongodb://localhost:27017/hotel_booking"
    mongo = PyMongo(app)
    return mongo

def add_hotel(hotel_data):
    mongo.db.hotels.insert_one(hotel_data)

def get_hotels():
    return list(mongo.db.hotels.find({}, {"_id": 0}))

def get_hotel_by_name(name):
    return mongo.db.hotels.find_one({"name": name}, {"_id": 0})

def update_hotel(name, update_data):
    return mongo.db.hotels.update_one({"name": name}, {"$set": update_data})

def delete_hotel(name):
    return mongo.db.hotels.delete_one({"name": name})
