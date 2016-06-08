__author__ = 'Administrator'
from pymongo import MongoClient
import re
def PageResults(collection, skip):
    # query = {"name":{"$regex":r'BJ'}}
    query = {"name":re.compile('BJ')}
    cursor = collection.find(query)
    # print(cursor.count())
    cursor.limit(10)
    cursor.skip(skip)
    print("Page " + str(skip + 1) + " to " + \
        str(skip + cursor.count(True)) + ":")
    for doc in cursor:
        print(doc)

    if(cursor.count(True) == 10):
        PageResults(collection, skip + 10)
    # print(cursor)

if __name__ == "__main__":
    mongo = MongoClient('mongodb://localhost:27017/')
    db=mongo['BeiJingDomain']
    collectionDevice = db["Device"]
    PageResults(collectionDevice,0)