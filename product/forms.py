# Imports
from django import forms
from .models import Category, Product, InputOfProduct, OutputOfProduct, Stock


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class ProductForm(forms.ModelForm):
    value = forms.CharField(label="Valor")
    unit_size = forms.FloatField(label="Tamanho", min_value=0)
    
    class Meta:
        model = Product
        fields = ['category', 'name', 'description',
                 'value', 'type_of_measure', 'unit_size']

    def clean_value(self):
        print(self.cleaned_data['value'])
        value = self.cleaned_data['value'][:-3]
        print("---")
        print(value)

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

        return quantity