from django.contrib import admin
from app.models import Book,Transaction

class RegisterBook(admin.ModelAdmin):
    pass
admin.site.register(Book, RegisterBook)

class RegisterTransaction(admin.ModelAdmin):
    pass
admin.site.register(Transaction, RegisterTransaction)



