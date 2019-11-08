from django.db import models


class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    published = models.DateField()
    genre = models.TextField()
    in_stock = models.BooleanField()
    description = models.TextField(null=True)


class Transaction(models.Model):
    datetime = models.DateField()
    action = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

