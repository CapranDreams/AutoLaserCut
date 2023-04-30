from pymongo import MongoClient

def get_database(db_name):
    #CONNECTION_STRING = "mongodb+srv://________________________________________________________________"
    client = MongoClient(CONNECTION_STRING)
    return client, client[db_name]

def get_collection(db_name, collection_name):
    _, db_handle = get_database(db_name)
    return db_handle[collection_name]

def get_records(table):
    result = []
    for i in table.find({}):
        result.append(i)
    return result

def new_record(_name, _type, _fileaddr):
    # Create a new record (does not add it to the database yet)
    record = {
        'name': _name, 
        'type': _type, 
        'file': _fileaddr
    } 
    return record
def new_image_record(_name, _fileaddr):
    # Create a new record (does not add it to the database yet)
    record = {
        'name': _name, 
        'file': _fileaddr
    } 
    return record

def add_record(table, record):
    # Add a record to the database collection (table)
    table.insert_one(record)

myCollection = get_collection('toolpaths', 'tp')

