import dramatiq

from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

import environ, os, yt_dlp
import time

# django only wants relative imports, dramatiq HATES them.
try:
    from dlp.hook import dlp_logger, stathook
except:
     from .dlp.hook import dlp_logger, stathook

import pprint

@dramatiq.actor
def play():
     # get environment file
        env = environ.Env()
        environ.Env.read_env()

        # mongussy auth, obviously
        login_string = "mongodb+srv://{usr}:{pwd}@{addr}/?retryWrites=true&w=majority&appName=Cluster0".format(usr=env('mongousr'), pwd=env('mongopwd'), addr=env('mongoadr'))
        print(login_string)
        client = MongoClient(login_string, server_api=ServerApi('1'))

        # get big ahh list of posts
        db = client['arrrdio']
        collection = db['arrrdio-play']
        posts = collection.posts

        print("play loop")

        while True:
            for post in collection.find():
                u = post["_entry"]["address"]
                os.system(f"ffplay -nodisp -autoexit c:/tmp/{u}.m4a")

                filter = {"_id": post["_id"]}
                res = collection.delete_one(filter)
                res = None
            
            if collection.count_documents({}) == 0: # if there were songs added during the loop, rerun it!
                with collection.watch() as stream:
                    for change in stream:
                        break # change has been pushed to database, replay songs!
     

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
        collection = db['arrrdio-dl']
        sync_target = db['arrrdio-play']

        print("dl loop")

        play.send()

        while True:
             
            for post in collection.find():
                pprint.pprint(post)
                print(post["_entry"]["_trackInfo"]["title"])
                u = post["_entry"]["address"]
                url = f"https://youtu.be/{u}"
                print(url)

                ydl_opts = {
                    'format': 'm4a/bestaudio/best',
                    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
                    'postprocessors': [{  # Extract audio using ffmpeg
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'm4a',
                    }],
                    'outtmpl': f'C:/tmp/{u}.%(ext)s',
                    'logger': dlp_logger(),
                    'progress_hooks': [stathook]
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    error_code = ydl.download(url)

                filter = {"_id": post["_id"]}

                # download complete!
                res = collection.delete_one(filter)
                res = sync_target.insert_one(post).inserted_id
                res = None
            # list is done, start watching for changes
            with collection.watch() as stream:
                for change in stream:
                    break # change has been pushed to database, redownload songs!


@dramatiq.actor
def addsong(data):
    env = environ.Env()
    environ.Env.read_env()
    login_string = "mongodb+srv://{usr}:{pwd}@{addr}/?retryWrites=true&w=majority&appName=Cluster0".format(usr=env('mongousr'), pwd=env('mongopwd'), addr=env('mongoadr'))
    print(login_string)
    client = MongoClient(login_string, server_api=ServerApi('1'))

    db = client['arrrdio']
    collection = db['arrrdio-dl']

    temp_posts = collection.insert_one(data).inserted_id # we do not care for this !!!!!!

    print("Added to queue | " + data["_entry"]["_trackInfo"]["title"])
              
              
# Debug tasks
@dramatiq.actor
def sync_dummy_data():
    env = environ.Env()
    environ.Env.read_env()

    login_string = "mongodb+srv://{usr}:{pwd}@{addr}/?retryWrites=true&w=majority&appName=Cluster0".format(usr=env('mongousr'), pwd=env('mongopwd'), addr=env('mongoadr'))
    print("mongo auth woob")

    client = MongoClient(login_string, server_api=ServerApi('1'))
    db = client['arrrdio']
    sync_src = db['arrrdio']
    sync_target = db['arrrdio-dl']

    for post in sync_src.find():
        temp_posts = sync_target.insert_one(post).inserted_id