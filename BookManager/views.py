from django.shortcuts import render
from .models import Book, Author, Genre

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.


def index(request):
    books = Book.objects.all()

    bookInformation = {}

    for book in books:
        bookInformation[book.title] = {
            author: [],
            genre: [],
        }

    authors = Author.objects.all()
    genres = Genre.objects.all()

    for author in authors:
        # add author name to book by the name of author.book
        bookInformation[author.book].author.append(author.name)

    for genre in genres:
        # add genre name to genre.book
        bookInformation[genre.book].genre.append(genre.genre)

    return render(request, "BookManager/index.html", {
        "books": books,
        "bookInformation": bookInformation
    })


def searchAuthor(request, name):
    books = Book.objects.filter(author=name)
    return render(request, "BookManager/index.html", {
        "books": books
    })


def searchTitle(request, name):
    books = Book.objects.filter(title=name)
    return render(request, "BookManager/index.html", {
        "books": books
    })
