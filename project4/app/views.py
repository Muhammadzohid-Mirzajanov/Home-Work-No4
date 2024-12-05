from django.shortcuts import render
from .models import Author, Book, Review


def authors_list(request):
    authors = Author.objects.all()
    return render(request, "authors.html", {"authors": authors})


def books_list(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
