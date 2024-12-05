from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.authors_list, name='authors_list'),
    path('books/', views.books_list, name='books_list'),
    path('reviews/', views.reviews_list, name='reviews_list'),
]