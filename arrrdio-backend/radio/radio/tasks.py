from celery import Celery

from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

import environ

import json

app = Celery('basks', broker='pyamqp://guest@localhost//')

@app.task
def resume():
    start()

@app.task
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

        for post in posts.find():
            pprint.pprint(post)
            y = json.loads(post)
            print(y["_entry"]["_trackinfo"]["title"])
            print(y["_entry"]["address"])

              
              
