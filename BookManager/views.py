from django.shortcuts import render
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def fillBookKeys(books):
    bookInformation = {}
    for book in books:
        bookInformation[book.title] = {
            "author": [],
            "genre": [],
        }
    return bookInformation


def renderAllBooks(request, location):
    bookDictionary = bookDictionaryInit(Book.objects.all())
    context = sortBookInformation(
        bookDictionary["books"], bookDictionary["bookInformation"])

    return render(request, location, context)


def bookDictionaryInit(books):
    bookInformation = fillBookKeys(books)

    authors = Author.objects.all()
    genres = Genre.objects.all()

    for author in authors:
        book = str(author.book)
        if (book in bookInformation):
            bookData = bookInformation[book]
            bookAuthorList = bookData["author"]
            bookAuthorList.append(author.name)

    for genre in genres:
        book = str(genre.book)
        if (book in bookInformation):
            bookData = bookInformation[book]
            bookGenreList = bookData["genre"]
            bookGenreList.append(genre.genre)

    return {
        "books": books,
        "bookInformation": bookInformation
    }


def sortBookInformation(books, bookInformation):
    authors = []
    genres = []

    for book in books:
        authors.append(bookInformation[book.title]["author"])
        genres.append(bookInformation[book.title]["genre"])

    return {
        "booksInfo": zip(books, authors, genres)
    }


def index(request):
    return renderAllBooks(request, "BookManager/index.html")


def searchTitle(request):
    if request.method == "GET":
        query = request.GET.get("title")

        if (query == ""):
            return index(request)

        bookDictionary = bookDictionaryInit(Book.objects.filter(title=query))
        context = sortBookInformation(
            bookDictionary["books"], bookDictionary["bookInformation"])

        return render(request, "BookManager/index.html", context)

    else:
        return index(request)


def searchAuthor(request):
    if request.method == "GET":
        query = request.GET.get("fname")

        if (query == ""):
            return index(request)

        bookDictionary = bookDictionaryInit(Book.objects.all())
        bookDictionary = bookDictionary["bookInformation"]

        filteredBooks = filterBookDictionaryByAuthor(query, bookDictionary)

        books = Book.objects.filter(title__in=filteredBooks)

        context = sortBookInformation(
            books, bookDictionary)

        return render(request, "BookManager/index.html", context)
    else:
        return index(request)


def filterBookDictionaryByAuthor(query, bookInformation):
    filteredBooks = []

    for book in bookInformation.copy():
        if query in bookInformation[book]["author"]:
            filteredBooks.append(book)
        else:
            bookInformation.pop(book)
    return filteredBooks


def editBooks(request):
    return renderAllBooks(request, "BookManager/edit.html")


def addBook(request):
    if request.method == 'POST':
        bookForm = BookForm(request.POST)
        authorForm = AuthorForm(request.POST)
        genreForm = GenreForm(request.POST)

        if bookForm.is_valid() and authorForm.is_valid() and genreForm.is_valid():
            new_title = bookForm.cleaned_data['title']
            new_pages = bookForm.cleaned_data['pages']
            new_publisher = bookForm.cleaned_data['publisher']
            new_quote = bookForm.cleaned_data["quote"]
            new_name = authorForm.cleaned_data["name"]
            new_genre = genreForm.cleaned_data["genre"]

            new_book = Book(
                title=new_title,
                pages=new_pages,
                publisher=new_publisher,
                quote=new_quote,
            )

            new_author = Author(
                name=new_name,
                book=new_book
            )

            new_genre = Genre(
                genre=new_genre,
                book=new_book
            )

            new_book.save()
            new_author.save()
            new_genre.save()
            return render(request, 'BookManager/add.html', {
                'success': True
            })
        else:
            bookForm = BookForm()
            genreForm = GenreForm()
            authorForm = AuthorForm()

    return render(request, 'BookManager/add.html', {
        "bookForm": BookForm(),
        "authorForm": AuthorForm(),
        "genreForm": GenreForm()
    })


def updateBook(request, id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)
        bookForm = BookForm(request.POST, instance=book)

        if bookForm.is_valid():
            bookForm.save()
            return render(request, 'BookManager/update.html', {
                'form': bookForm,
                'success': True
            })
    else:
        book = Book.objects.get(pk=id)
        bookForm = BookForm(instance=book)
    return render(request, 'BookManager/update.html', {
        'form': bookForm
    })


def deleteBook(request, id):
    if request.method == "POST":
        book = Book.objects.get(pk=id)
        book.delete()
    return HttpResponseRedirect(reverse('edit'))
