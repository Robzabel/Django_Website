from django.urls import path
from . import views

#Define the path to the view and give it an alias
urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("create/", views.create, name="create"),
]
