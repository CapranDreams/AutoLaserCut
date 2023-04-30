from pymongo import MongoClient
import random

def get_database():
    # Retrurns the database object
    CONNECTION_STRING = "mongodb+srv://sasha:ON9beYlXRy1QBe83@testmongo.94agqyf.mongodb.net/toolpaths"
    client = MongoClient(CONNECTION_STRING)
    return client['toolpaths']  # database name is 'toolpaths'
  
def new_record(_name, _type, _fileaddr):
    # Create a new record (does not add it to the database yet)
    record = {
        'name': _name, 
        'type': _type, 
        'file': _fileaddr
    } 
    return record

def add_record(table, record):
    # Add a record to the database collection (table)
    rec = table.insert_one(record)

def get_record(table, name):
    # Gets a record with the name specified
    result = []
    for i in table.find({'name': name}):
        result.append(i)
        #print(i)
    return result
        
def get_record_type(table, _type):
    # Gets a record with the name specified
    for i in table.find({'type': _type}):
        print(i)

def create_random_record(collection):
    rn = random.randrange(100000)
    rt = random.randrange(100000)
    rf = random.randrange(100000)
    rec = new_record(rn, rt, rf)
    add_record(collection, rec)
    return rn

if __name__ == "__main__":   
    print("\n")

    # Get the database
    myDB = get_database()
    myCollection = myDB['test']

    # Add record to the database
    #rn = create_random_record(myCollection)

    # Find this record to the database and print it out
    #res = get_record(myCollection, rn)

    print(myCollection.count_documents({}))
