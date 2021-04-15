import datetime
from pymongo import MongoClient
from pprint import pprint
client = MongoClient('localhost', 27017)
db = client['mongo_db_lab']
coll = db['definitions']


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''

    # random selection: idea from https://stackoverflow.com/questions/2824157/random-record-from-mongodb
    sample = coll.aggregate([{'$sample': {'size': 1}}]).next()
    print('Before:')
    pprint(sample)
    print()

    timestamp = datetime.datetime.utcnow().isoformat()
    coll.update_one({'_id': sample['_id']}, {
        '$push': {'dates': timestamp}})
    print('After:')
    pprint(coll.find_one({'_id': sample['_id']}))
    return


if __name__ == '__main__':
    random_word_requester()
