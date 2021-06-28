from django.shortcuts import render
from .models import ToDoList, Item
from django.http import HttpResponse#
from .forms import Create_new_list

"""def index(response, id):
    return HttpResponse("<h1> hello world</h1>") # this uses httpresponse so doesnt need to return the response argument passesd to it
"""

def home(response):
    return render( response,  "main/home.html", {}) #this uses the render module so needs to return the response argument passed to it


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'main/list.html', {"ls": ls})


def create(response):
    form = Create_new_list()
    return render( response, "main/create.html", {"form":form})
