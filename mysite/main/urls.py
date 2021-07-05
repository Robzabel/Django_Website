from django.urls import path
from . import views

#Define the path to the view and give it an alias
urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.view, name="view"),
path("home/", views.home, name="home"),
path("create/", views.create, name="create"),
path("view/", views.view, name="view"),
]
