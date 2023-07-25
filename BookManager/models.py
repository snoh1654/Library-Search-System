from django.db import models

# Create your models here


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.genre}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ForeignKey(
        Author, on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=50)
    quote = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.authors}"
