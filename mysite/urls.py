from django.urls import path
from .views import *

urlpatterns = [
    path("home/", HomeView, name="home"),
    path("form/", FormView, name="form"),
    path("edit/<pk>/", edit_todo, name="edit"),
    path("delete/<pk>/", delete, name="delete"),
]
