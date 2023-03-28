from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://sasha:ON9beYlXRy1QBe83@testmongo.94agqyf.mongodb.net/toolpaths"
client = pymongo.MongoClient(CONNECTION_STRING)

# Database name
db = client['toolpaths']

# Collection object
table = db['tp']
