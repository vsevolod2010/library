from library.celery import app
from .models import Author, Book


@app.task
def books_calc():
    books = Book.objects.count()
    return books


@app.task
def authors_calc():
    authors = Author.objects.count()
    return authors

