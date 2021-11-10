# Imports
from django import forms
from .models import Sale, ItemSale


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['card', 'status']


class ItemSaleForm(forms.ModelForm):
    class Meta:
        model = ItemSale
        fields = '__all__'
        exclude = ('unitary_value', 'total', 'sale')