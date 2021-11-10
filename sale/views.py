# Imports
from datetime import datetime

from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

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
        return context