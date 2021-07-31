from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


# Create your models here.
class Book(models.Model):
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
