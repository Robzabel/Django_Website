from django.db import models
from django.contrib.auth.models import User
#create the to do list model
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)


    #define a str method so the API can retrieve the data
    def __str__(self) -> str:
        return f"<Todo Name: {self.name}>"


#Create the Item model that will be linked to the ToDoList model 
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    #define a str method so the API can retrieve the data
    def __str__(self) -> str:
        return f"<Item: {self.text}>"