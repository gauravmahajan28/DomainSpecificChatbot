import re
import pymongo
client = pymongo.MongoClient('mongodb://user:password123@ds123963.mlab.com:23963/project', connectTimeoutMS=300000)
db = client.get_default_database()
flipkart_data = db.flipkart_data


for document in flipkart_data.find():
    print(document) # iterate the cursor
k = 0;