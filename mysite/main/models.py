from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)


    def __repr__(self) -> str:
        return f"<Todo Name: {self.name}>"
    