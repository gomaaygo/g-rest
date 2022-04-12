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
    quantity = forms.IntegerField(label="Quantidade", min_value=1, required=True)

    class Meta:
        model = ItemSale
        fields = '__all__'
        exclude = ('unitary_value', 'total', 'sale')


class SnackForm(forms.ModelForm):
    product = forms.ModelChoiceField(label="Refeição", queryset=Product.objects.filter(category__name="Refeição"))
    quantity_snack = forms.IntegerField(required=True)

    class Meta:
        model = ItemSale
        fields = ['product', 'quantity_snack']
        exclude = ('unitary_value', 'total', 'sale', 'quantity')