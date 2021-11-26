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
from .forms import OpenSaleForm, ItemSaleForm, CloseSaleForm, SnackForm
from account.permissions import GroupRequiredMixin


class SaleOpenListView(ListView):
    model = Sale
    template_name = 'sale/sale_open_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Sale.objects.filter(status='open').order_by("card")
        context['form'] = OpenSaleForm()

        return context


class SaleDetailView(DetailView):
    model = Sale

    def get_sale(self):
        return get_object_or_404(Sale, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sale = self.get_sale()
        context['sale'] = sale
        context['items'] = ItemSale.objects.filter(sale=sale.pk).order_by("-pk")
        context['form_item_sale'] = ItemSaleForm()
        context['form_sale'] = CloseSaleForm()
        context['form_add_snack'] = SnackForm()

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


def add_snack(request, pk):
    sale = Sale.objects.get(id=pk)
    form_snack = SnackForm(request.POST)

    if form_snack.is_valid():
        product = Product.objects.get(id=form_snack.cleaned_data['product'].pk)

        try:
            item = ItemSale.objects.get(product=product.pk, sale=sale.pk, sale__status="open")

            item.quantity=item.quantity+form_snack.cleaned_data['quantity']
            item.total=new_quantity*product.value
            item.save()

            messages.success(request, "Refeição adicionada com sucesso!")
            return redirect(reverse('sale:sale-detail', args=[sale.pk]))

        except:
            item_sale = ItemSale.objects.create(
                product=product,
                quantity_snack=form_snack.cleaned_data['quantity_snack'],
                unitary_value=product.value,
                total=form_snack.cleaned_data['quantity_snack']*product.value,
                sale=sale
            )

            messages.success(request, "Refeição adicionada com sucesso!")
            return redirect(reverse('sale:sale-detail', args=[sale.pk]))


def new_sale(request):
    card = Card.objects.get(id=request.POST['card'])
    card.status = "not_available"
    card.save()

    item_sale = Sale.objects.create(
        card=card
    )

    sale = Sale.objects.get(card=card, status="open")

    messages.success(request, "Comanda aberta com sucesso!")
    return redirect(reverse('sale:sale-detail', args=[sale.pk]))


def close_sale(request, pk):
    sale = Sale.objects.get(id=pk)
    items = ItemSale.objects.filter(sale=sale)
    total = 0

    for item in items:
        total = total+item.total

    sale.type_of_payment = request.POST['type_of_payment']
    sale.total = total
    sale.status = "closed"
    sale.save()

    card = Card.objects.get(id=sale.card.pk)
    card.status = "available"
    card.save()

    messages.success(request, "Venda encerrada com sucesso!")
    return redirect(reverse('sale:sale-open-list'))


class SaleListView(GroupRequiredMixin, ListView):
    group_required = [u'Gerente']
    model = Sale
    queryset = Sale.objects.all().order_by("-sale_date")