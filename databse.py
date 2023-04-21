import json
from datetime import time

import requests as requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://RootUser:Raman1234@cluster0.sfqudim.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    db = client["CurrenData"]
    column = db["Cur"]

    key = "https://api.freecurrencyapi.com/v1/latest?apikey=nvUKgmNqxOI9GXCN3ZXc59K4nkIaNwWeWQIFAoMd"
    data = {}
    r = requests.get(key)
    d = r.json()
    json_string = json.dumps(d['data'])

    dict = json.loads(json_string);
    print(dict)
    column.insert_one(dict)

    time.sleep(86400);
except Exception as e:
    print(e)


