# Imports
from datetime import datetime

from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages

from product.models import Product
from .models import Sale, Card, ItemSale
from .forms import SaleForm, ItemSaleForm


class SaleOpenListView(ListView):
    model = Sale
    queryset = Sale.objects.filter(status='open')
    template_name = 'sale/sale_open_list.html'


class SaleDetailView(DetailView):
    model = Sale

    def get_sale(self):
        return get_object_or_404(Sale, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sale = self.get_sale()
        context['sale'] = sale
        context['items'] = ItemSale.objects.filter(sale=sale.pk).order_by("-pk")
        context['form'] = ItemSaleForm()

        return context


def add_item_sale(request, pk):
    sale = Sale.objects.get(id=pk)
    form_item_sale = ItemSaleForm(request.POST)

    if form_item_sale.is_valid():
        product = Product.objects.get(id=form_item_sale.cleaned_data['product'].pk)

        try:
            item = ItemSale.objects.get(product=product.pk, sale=sale.pk, sale__status="open")
            
            new_quantity = item.quantity+form_item_sale.cleaned_data['quantity']

            item.quantity=new_quantity
            item.total=new_quantity*product.value
            item.save()

            messages.success(request, "Item adicionado com sucesso!")
            return redirect(reverse('sale:sale-detail', args=[sale.pk]))

        except:
            item_sale = ItemSale.objects.create(
                product=product,
                quantity=form_item_sale.cleaned_data['quantity'],
                unitary_value=product.value,
                total=form_item_sale.cleaned_data['quantity']*product.value,
                sale=sale
            )

            messages.success(request, "Item adicionado com sucesso!")
            return redirect(reverse('sale:sale-detail', args=[sale.pk]))