# Imports
from django import forms
from .models import Sale, ItemSale, Card


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
    class Meta:
        model = ItemSale
        fields = '__all__'
        exclude = ('unitary_value', 'total', 'sale')