from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("edit-books", views.editBooks, name="edit"),
    path("search-title", views.searchTitle, name="search-title"),
    path("search-author", views.searchAuthor, name="search-author")

]
