from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
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
        author_id = request.GET.get('id')
        if author_id is not None:
            author = Author.objects.get(id=author_id)
        else:
            author = None
        return render(request, 'addAuthorForm.html', {'author':author})

    def post(self, request):
        imie = request.POST.get('first_name')
        nazwisko = request.POST.get('last_name')
        a = Author.objects.create(first_name=imie, last_name=nazwisko)
        url = reverse('add_author') + f"?id={a.id}"
        return redirect(url)


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