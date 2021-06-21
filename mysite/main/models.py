from django.db import models

#create the to do list model
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    #define a repr function to give information to the user
    def __repr__(self) -> str:
        return f"<Todo Name: {self.name}>"

    #define a str method so the API can retrieve the data
    def __str__(self) -> str:
        return f"<Todo Name: {self.name}>"


#Create the Item model that will be linked to the ToDoList model 
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    #define a repr function to give information to the user
    def __repr__(self) -> str:
        return f"<Item: {self.text}>"

    #define a str method so the API can retrieve the data
    def __str__(self) -> str:
        return f"<Item: {self.text}>"