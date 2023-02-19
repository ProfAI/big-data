import pandas as pd
from pymongo import MongoClient
import os

def get_database():
    CONNECTION_STRING = "mongodb://root:example@127.0.0.1/"

    client = MongoClient(CONNECTION_STRING)

    return client['crypto']

if __name__ == "__main__":

    mypath = './parquet'
    dbname = get_database()
    collection_name = dbname["reddit"]

    for file in os.listdir(mypath):
        posts = pd.read_parquet(os.path.join(mypath, file))
        out = posts.to_dict('records')
        collection_name.insert_many(out)