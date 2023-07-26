from django.db import models

# Create your models here


class Book(models.Model):
    title = models.CharField(max_length=50)

    pages = models.PositiveIntegerField()

    publisher = models.CharField(max_length=50)
    quote = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"


class Author(models.Model):
    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    genre = models.CharField(max_length=20)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.genre}"
