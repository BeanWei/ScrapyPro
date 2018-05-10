# table IPPORT
# ip_port TEXT NOT NULL
import traceback
import Config
import pymongo


MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'test'

client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client[MONGO_DB]

def AddItem(ip_port):
    db.ippool.save({"ip": ip_port})

def AddItems(ip_list):
    if not ip_list:
        return

    db.ippool.insert_many([{"ip": ip_port} for ip_port in ip_list])

def DelItem(item):
    db.ippool.delete_one({"ip": item})

def ClearItems():
    db.ippool.remove({})

def GetItems():
    db.ippool.find()
