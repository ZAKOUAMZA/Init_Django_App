from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
def index(request):
    context = {
        "message": "Hello, world !",
        "Number":15,
        "list":["tata","toto","titi"],
        "publication": datetime.datetime.now,
        "username":"Amza",
        "description":"lorem ipsum dolor sit amet consectetur",
        "list2":["tati","toti","tita"],
        "numberOfNews":1

    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context,request))
