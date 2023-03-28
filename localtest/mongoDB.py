from pymongo import MongoClient

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

if __name__ == "__main__":   
  
    # Get the database
    myDB = get_database()
    myCollection = myDB['tp']

    # Add this record to the database
    my_first_record = new_record('testRect', 'box', '/autolasercut/toolpaths/testRect.svg')
    add_record(myCollection, my_first_record)

    # Add this record to the database
    my_second_record = new_record('40deep', 'box', '/autolasercut/toolpaths/40deep.svg')
    add_record(myCollection, my_second_record)

    # Find this record to the database and print it out
    get_record(myCollection, 'testRect')
