from django import forms
from .models import Book, Author, Genre


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "pages", "publisher", "quote"]
        labels = {
            "title": "Book Title",
            "pages": "Page Count",
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]
        labels = {
            "name": "Author Name"
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["genre"]
