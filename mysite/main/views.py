from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoList, Item
from django.http import HttpResponseRedirect
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
    if response.method == "POST":
        form = Create_new_list(response.POST) #take the data from the POST request and add it to the form

        if form.is_valid(): #validate the form data received in the POST request
            n = form.cleaned_data["name"]#clean the data and grab the name value
            t = ToDoList(name=n) #pass the name to the list argument
            t.save() #save the new to do list to the database

        return HttpResponseRedirect("/%i" %t.id) #redirect to the todo list page

    else:
        form = Create_new_list()
    return render( response, "main/create.html", {"form":form})
