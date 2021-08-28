# Imports
from django.contrib import admin
from .models import Category, Product, Stock


# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'value',]


class StockModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'quantity_min',]


admin.site.register(Category)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Stock, StockModelAdmin)

