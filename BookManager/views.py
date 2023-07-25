from django.shortcuts import render
from .models import Book

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "BookManager/index.html", {
        "books": Book.objects.all()
    })
