"""ONLPYT8W URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jej import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.NameListView.as_view(), name='list_view'),
    path('add_author/', views.AddAuthorView.as_view(), name='add_author'),
    path('add_author_by_form/', views.AddAuthorByFormView.as_view(), name='add_author_by_form'),
    path('list_author/', views.ListAuthorView.as_view(), name='list_author'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('add_book_by_form/', views.AddBookByFormView.as_view(), name='add_book_by_form'),
    path('list_book/', views.ListBookView.as_view(), name='list_book'),
]
