from django.shortcuts import render, redirect
from app.models import Book, Transaction
from datetime import datetime
from django.contrib import messages


def home(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})



def borrow_book(request, id):
    book = Book.objects.get(id=id)
    new_transaction = book.transaction_set.create(
        datetime=datetime.now(), action="CHECKOUT"
    )
    if book.in_stock:
        book.in_stock = False
        messages.success(request, f'Borrowed {book.title} by { book.author }')
        book.save()
        return redirect("home")
    else:
        messages.error(request, f'{book.title} by { book.author } is unavailable')
        return redirect("home")


def return_book(request, id):
    book = Book.objects.get(id=id)
    new_transaction = book.transaction_set.create(
        datetime=datetime.now(), action="CHECKIN"
    )
    if book.in_stock:
        book.in_stock = True
        messages.error(request, f'{book.title} by { book.author } is already here')
        book.save()
        return redirect("home")
    else:
        messages.success(request, f'Returned {book.title} by { book.author }')
        return redirect("home")

