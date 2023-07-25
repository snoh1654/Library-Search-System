from django import forms
from .models import Book

title = None


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages', 'publisher', 'quote']
        labels = {
            'title': 'Book Title',
            'pages': 'Page Count',
            'publisher': 'Publisher',
            'quote': 'Quote'
        }

# class AuthorForm()
