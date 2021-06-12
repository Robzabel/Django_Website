from django.urls import path
from . import views

#Define the path to the view and give it an alias
urlpatterns = [
    path("", views.index, name="index"),
]
