from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("/author/<str:name>", views.searchAuthor, name="search-author"),
    path("/title/<str:name>", views.searchTitle, name="search-title")
]
