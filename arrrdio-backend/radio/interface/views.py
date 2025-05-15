from django.http import HttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt

import environ

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
def add(request):
    if request.method != "POST":
        return HttpResponse(status=400)
    else:
        env = environ.Env()
        environ.Env.read_env()
        login_string = "mongodb+srv://{usr}:{pwd}@{addr}/?retryWrites=true&w=majority&appName=Cluster0".format(usr=env('mongousr'), pwd=env('mongopwd'), addr=env('mongoadr'))
        print(login_string)