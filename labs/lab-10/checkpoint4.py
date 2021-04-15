from pymongo import MongoClient
import pprint
client = MongoClient('localhost', 27017)

if __name__ == '__main__':
    db = client['mongo_db_lab']
    definitions = db['definitions']

    # print all entries
    print('Fetch all entries')
    for definition in definitions.find():
        pprint.pprint(definition)

    print('-' * 20)
    print()

    # print one entry
    print('Fetch one entry')
    entry = definitions.find_one()
    pprint.pprint(entry)

    print('-' * 20)
    print()

    # print one specific entry
    print('Fetch a specific entry')
    entry = definitions.find_one({'word': 'Ultor'})
    pprint.pprint(entry)
    print('-' * 20)
    print()

    # find entry by object id
    print('Fetch a specific entry with object id')
    def_id = entry['_id']
    pprint.pprint(definitions.find_one({'_id': def_id}))
    print('-' * 20)
    print()

    print('Insert a new record')
    entry = {'word': 'hi', 'definition': 'Hello World!'}
    entry_id = definitions.insert_one(entry).inserted_id
    print(f'ID of inserted document: {entry_id}')

    # print("Modify me")
