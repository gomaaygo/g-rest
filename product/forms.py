# Imports
from django import forms
from .models import Category, Product, InputOfProduct, OutputOfProduct


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    value = forms.DecimalField(label="Valor", min_value=0.0)
    unit_size = forms.FloatField(label="Tamanho", min_value=0)
    
    class Meta:
        model = Product
        fields = ['category', 'name', 'description',
                 'value', 'type_of_measure', 'unit_size']


class InputOfProductForm(forms.ModelForm):
    class Meta:
        model = InputOfProduct
        fields = ['product', 'quantity', 'expiration_date']


class OutputOfProductForm(forms.ModelForm):
    class Meta:
        model = OutputOfProduct
        fields = ['product', 'quantity']