# Imports
from django import forms
from .models import Sale, ItemSale, Card


class SaleForm(forms.ModelForm):
    card = forms.ChoiceField(choices=[('0', '--Selecione--')] + [(card.id, card.id) for card in Card.objects.filter(status="available").order_by("pk")])

    class Meta:
        model = Sale
        fields = ['card']


class ItemSaleForm(forms.ModelForm):
    class Meta:
        model = ItemSale
        fields = '__all__'
        exclude = ('unitary_value', 'total', 'sale')