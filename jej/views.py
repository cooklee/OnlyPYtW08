from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View

from jej.forms import AddAuthorForm, AddBookForm, AddBookModelForm
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
        return render(request, 'addAuthorForm.html', {'author': author, 'user': 'a to ci niespodzianka'})

    def post(self, request):
        imie = request.POST.get('first_name')
        nazwisko = request.POST.get('last_name')
        a = Author.objects.create(first_name=imie, last_name=nazwisko)
        url = reverse('add_author') + f"?id={a.id}"
        return redirect(url)


class AddAuthorByFormView(View):
    def get(self, request):
        form = AddAuthorForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            imie = form.cleaned_data.get('first_name')
            nazwisko = form.cleaned_data.get('last_name')
            a = Author.objects.create(first_name=imie, last_name=nazwisko)
            return redirect('list_author')
        return render(request, 'form.html', {'form': form})


class AddBookView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'addBookForm.html', {'authors': authors})

    def post(self, request):
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        author = Author.objects.get(pk=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('add_book')

class AddBookByFormView(View):
    def get(self, request):
        form = AddBookModelForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddBookModelForm(request.POST)
        if form.is_valid():

            # title = form.cleaned_data.get('title')
            # author = form.cleaned_data.get('author')
            #a = Book.objects.create(title=title, author=author)

            # a = Book.objects.create(**form.cleaned_data)
            book = form.save()

            return redirect('list_book')
        return render(request, 'form.html', {'form': form})





class ListAuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'object_list.html', {'objects': authors})


class ListBookView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'object_list.html', {'objects': books})
