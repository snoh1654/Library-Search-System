from django.shortcuts import render
from .models import Book, Author, Genre

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.


def bookHelper(request, books):
    bookInformation = {}

    for book in books:
        bookInformation[book.title] = {
            "author": [],
            "genre": [],
        }

    authors = Author.objects.all()
    genres = Genre.objects.all()

    for author in authors:
        if (str(author.book) in bookInformation):
            bookInformation[str(author.book)]["author"].append(author.name)

        # add author name to book by the name of author.book

    for genre in genres:
        if (str(genre.book) in bookInformation):
            bookInformation[str(genre.book)]["genre"].append(genre.genre)

        # add genre name to genre.book

    return {
        "books": books,
        "bookInformation": bookInformation
    }


def sortBookInformation(request, books, bookInformation):
    authors = []
    genres = []

    for book in books:
        authors.append(bookInformation[book.title]["author"])
        genres.append(bookInformation[book.title]["author"])

    return {
        "booksInfo": zip(books, authors, genres),
        "authors": authors,
        "genres": genres
    }


def index(request):
    returnBook = bookHelper(request, Book.objects.all())
    context = sortBookInformation(request,
                                  returnBook["books"], returnBook["bookInformation"])

    return render(request, "BookManager/index.html", context)


def searchAuthor(request):

    if request.method == "GET":
        query = request.GET.get("fname")

        if (query == ""):
            return index(request)

        print(query)

        bookHelperReturn = bookHelper(request, Book.objects.all())
        books = bookHelperReturn["books"]
        bookInformation = bookHelperReturn["bookInformation"]

        filterBooks = []

        for book in bookInformation.copy():
            if query in bookInformation[book]["author"]:
                filterBooks.append(book)
            else:
                bookInformation.pop(book)

        books = Book.objects.filter(title__in=filterBooks)

        print(books, "done")
        print(bookInformation)

        returnBook = {
            "books": books,
            "bookInformation": bookInformation
        }

        context = sortBookInformation(request,
                                      returnBook["books"], returnBook["bookInformation"])

        return render(request, "BookManager/index.html", context)
    else:
        return index(request)


def searchTitle(request):
    if request.method == "GET":
        query = request.GET.get("title")

        if (query == ""):
            return index(request)

        returnBook = bookHelper(request, Book.objects.filter(title=query))
        context = sortBookInformation(request,
                                      returnBook["books"], returnBook["bookInformation"])
        return render(request, "BookManager/index.html", context)
    else:
        return index(request)


def editBooks(request):
    return index(request)
