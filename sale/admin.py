# Imports
from django.contrib import admin
from .models import Card, ItemSale, Sale

# Register your models here.
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'status',]

class ItemSaleModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'unitary_value', 'total']

class SaleModelAdmin(admin.ModelAdmin):
    list_display = ['sale_date', 'status', 'type_of_payment', 'total']


admin.site.register(Card, CardModelAdmin)
admin.site.register(ItemSale, ItemSaleModelAdmin)
admin.site.register(Sale, SaleModelAdmin)