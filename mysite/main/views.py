from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
    get_list = ToDoList.objects.get(id=id)
    return HttpResponse(f"<h1>The name of the to do list is {get_list.name} </h1>")
