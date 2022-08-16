from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/new", views.new, name="new"),
    path("wiki/edit", views.edit, name="edit"),
    path("wiki/random", views.random_title, name="random"),
    path("wiki/<str:title>", views.get_title, name="title")
    
]
