from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from jej.models import Author, Book


class IndexView(View):

    def get(self, request, s='slawek'):
        httpResponse = render(request, 'base.html', {'name': s})
        return httpResponse


class NameListView(View):
    def get(self, request):
        lst = ['Slawek', 'gosia', 'kasia', 'basia', 'przemek', 'Piotr']
        httpResponse = render(request, 'listView.html', {'lst': lst})
        return httpResponse


class AddAuthorView(View):
    def get(self, request):
        return render(request, 'addAuthorForm.html')

    def post(self, request):
        imie = request.POST.get('first_name')
        nazwisko = request.POST.get('last_name')
        Author.objects.create(first_name=imie, last_name=nazwisko)
        return redirect('add_author')


class ListAuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'author_list.html', {'authors':authors})

class AddBookView(View):
    def get(self, request):
        return render(request, 'addBookForm.html')

    def post(self, request):
        title = request.POST.get('title')
        Book.objects.create(title=title)
        return redirect('add_book')


class ListBookView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book_list.html', {'books':books})