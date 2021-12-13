# Imports
import re
import decimal

from django import forms
from .models import Category, Product, InputOfProduct, OutputOfProduct, Stock


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    value = forms.CharField(label="Valor")
    unit_size = forms.FloatField(label="Tamanho", min_value=0)
    quantity_min = forms.IntegerField(label="Quantidade Mínima", min_value=0, required=False)
    
    class Meta:
        model = Product
        fields = ['category', 'name', 'description',
                 'value', 'type_of_measure', 'unit_size', 'quantity_min']

    def clean_value(self):
        value = int(re.sub('[^0-9]', '', self.cleaned_data['value']))/100
        value = round(decimal.Decimal(value), 2)

        return value


class InputOfProductForm(forms.ModelForm):
    class Meta:
        model = InputOfProduct
        fields = ['product', 'quantity', 'expiration_date']


class OutputOfProductForm(forms.ModelForm):
    class Meta:
        model = OutputOfProduct
        fields = ['product', 'quantity']

    def clean_quantity(self):
        stock = Stock.objects.get(product=self.cleaned_data['product'])
        if int(self.data['quantity']) > stock.quantity:
            raise forms.ValidationError("Quantidade disponível: " + str(stock.quantity))

        return self.data['quantity']