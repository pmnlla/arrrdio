from django.http import HttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt

from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

import json
import ofunctions.json_sanitize as of_sanitation

import environ

import pprint

from .tasks import start, addsong, sync_dummy_data

@csrf_exempt
def index(request):
    if request.method != "POST":
        html = """
        <html>
            <body>
                <form method="post">
                    <label for="textbox">Enter text:</label>
                    <input type="text" id="textbox" name="textbox">
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>
        """
        return HttpResponse(html)
    else:
        print(request.POST.items)
        return HttpResponse("good", status=200)

@csrf_exempt
def resume(request):
    start.send()
    return HttpResponse(status=200)

@csrf_exempt
def add(request):
    if request.method != "POST":
        return HttpResponse(status=400)
    else:
        data = json.loads(request.body)
        pprint.pprint(data)
        print(json.dumps(data))
        sanitized = of_sanitation.json_sanitize(data)

        if sanitized != data:
            return HttpResponse(status=418) # tried some weird shit with curl? fuck you!
        
        addsong.send(data)
        
        return HttpResponse(status=200)

        # by now, we should have the required data put into mongodb - which is all that we need!

@csrf_exempt
def sync(request):
    sync_dummy_data.send()
    return HttpResponse(status=200)