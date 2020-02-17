from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework import viewsets
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render
from .tasks import authors_calc, books_calc
from django.http import JsonResponse


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListView(ListView):

    context_object_name = 'library'
    template_name = 'library.html'

    def get_queryset(self):
        fltr = self.request.GET.get('fltr')
        if not fltr:
            fltr = ''
            books = Book.objects.all()
        else:
            books = Book.objects.filter(Q(title__icontains=fltr) | Q(authors__name__icontains=fltr))
        paginator = Paginator(books, 5)
        page = self.request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        books.fltr = fltr
        return books


class SearchBookListView(ListView):

    context_object_name = 'library'
    template_name = 'book_result.html'

    def get_queryset(self):
        fltr = self.request.GET.get('fltr')
        if fltr:
            books = Book.objects.filter(Q(title__icontains=fltr) | Q(authors__name__icontains=fltr))
        else:
            books = Book.objects.all()
        paginator = Paginator(books, 5)
        page = self.request.GET.get('page')
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        books.fltr = fltr
        return books


def books_count(request):
    books = books_calc.delay()
    books = books.get()
    return JsonResponse({'count': books})


def authors_count(request):
    authors = authors_calc.delay()
    authors = authors.get()
    return JsonResponse({'count': authors})


def statistic(request):
    return render(request, 'statistic.html', {'books': 'Идет подсчет...', 'authors': 'Идет подсчет...'})

