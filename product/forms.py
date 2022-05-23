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
    value = forms.CharField(label="Valor", required=False)
    unit_size = forms.FloatField(label="Tamanho", min_value=0, required=False)
    quantity_min = forms.IntegerField(label="Quantidade Mínima", min_value=0, required=False)
    purchase_price = forms.CharField(label="Valor de Compra", required=True)
    
    class Meta:
        model = Product
        fields = ['category', 'name', 'description',    
                 'value', 'type_of_measure', 'unit_size', 
                 'quantity_min', 'purchase_price', 'type_product']

    def clean(self):
        """
            1. Verifica se o campo value (valor de venda) está em branco e se 
            o produto é do tipo sale (venda), caso atenda essas condições
            uma exceção é executada.

            2. Verifica se o campo type_product é do tipo sale e se a categoria é
            None, se a condição for atendida uma exceção é executada.

            3. Verifica se o campo type_product é do tipo sale e se campo unity_size (tamanho)
            é None, caso atenda essa condição, uma exceção é executada.
        """
        cleaned_data = self.cleaned_data
        type_product = cleaned_data.get("type_product")
        value = cleaned_data.get("value")
        category = cleaned_data.get("category")
        unit_size = cleaned_data.get("unit_size")

        if (type_product == "sale" and value == None) or (type_product == "sale" and category == None) or (type_product == "sale" and unit_size == None):
            self._errors["value"] = forms.ValidationError("Este campo é obrigatório caso o produto seja para venda!")

        return cleaned_data


    def clean_value(self):
        if self.cleaned_data['value'] == "":
            return None
        else:
            value = int(re.sub('[^0-9]', '', self.cleaned_data['value']))/100
            value = round(decimal.Decimal(value), 2)

            return value

    def clean_purchase_price(self):
        purchase_price = int(re.sub('[^0-9]', '', self.cleaned_data['purchase_price']))/100
        purchase_price = round(decimal.Decimal(purchase_price), 2)

        return purchase_price


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