import dramatiq

from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

import environ

import json

import pprint


@dramatiq.actor
def start():
        
        # get environment file
        env = environ.Env()
        environ.Env.read_env()

        # mongussy auth, obviously
        login_string = "mongodb+srv://{usr}:{pwd}@{addr}/?retryWrites=true&w=majority&appName=Cluster0".format(usr=env('mongousr'), pwd=env('mongopwd'), addr=env('mongoadr'))
        print(login_string)
        client = MongoClient(login_string, server_api=ServerApi('1'))

        # get big ahh list of posts
        db = client['arrrdio']
        collection = db['arrrdio']
        posts = collection.posts

        print("weee")

        for post in collection.find():
            pprint.pprint(post)
            print(post["_entry"]["_trackInfo"]["title"])
            print(post["_entry"]["address"])

        print ("wooo")

@dramatiq.actor
def addsong(data):
    env = environ.Env()
    environ.Env.read_env()
    login_string = "mongodb+srv://{usr}:{pwd}@{addr}/?retryWrites=true&w=majority&appName=Cluster0".format(usr=env('mongousr'), pwd=env('mongopwd'), addr=env('mongoadr'))
    print(login_string)
    client = MongoClient(login_string, server_api=ServerApi('1'))

    db = client['arrrdio']
    collection = db['arrrdio']

    temp_posts = collection.insert_one(data).inserted_id # we do not care for this !!!!!!

    print("Added to queue | " + data["_entry"]["_trackInfo"]["title"])
              
              
