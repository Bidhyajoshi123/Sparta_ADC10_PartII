from django.contrib import admin
from .models import Customer, Depositor, Branch, Transaction, Account

# Register your models here.
admin.site.register(Customer)
admin.site.register(Depositor)
admin.site.register(Branch)
admin.site.register(Transaction)
admin.site.register(Account)
