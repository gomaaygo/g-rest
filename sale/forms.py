# Imports
from django import forms
from .models import Sale


class StartSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['card']