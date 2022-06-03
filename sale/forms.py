# Imports
from django import forms
from .models import Sale, ItemSale, Card, Product
from product.models import Product


class OpenSaleForm(forms.ModelForm):
    card = forms.ModelChoiceField(label="card", queryset=Card.objects.filter(status="available").order_by("pk"))

    class Meta:
        model = Sale
        fields = ['card']


class CloseSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['type_of_payment']


class ItemSaleForm(forms.ModelForm):
    product = forms.ModelChoiceField(label="Produto", queryset=Product.objects.filter(type_product="sale"))

    class Meta:
        model = ItemSale
        fields = '__all__'
        exclude = ('unitary_value', 'total', 'sale')


class SnackForm(forms.ModelForm):
    product = forms.ModelChoiceField(label="Refeição", queryset=Product.objects.filter(category__name="Refeição"))

    class Meta:
        model = ItemSale
        fields = ['product', 'quantity_snack']
        exclude = ('unitary_value', 'total', 'sale', 'quantity')