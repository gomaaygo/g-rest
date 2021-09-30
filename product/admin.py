# Imports
from django.contrib import admin
from .models import Category, Product, Stock, InputOfProduct, OutputOfProduct

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'value',]

class StockModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'quantity_min',]

class InputOfProductModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'entry_date', 'expiration_date']

class OutputOfProductModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'departure_date',]


admin.site.register(Category)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Stock, StockModelAdmin)
admin.site.register(InputOfProduct, InputOfProductModelAdmin)
admin.site.register(OutputOfProduct, OutputOfProductModelAdmin)


