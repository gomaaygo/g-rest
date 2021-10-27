# Imports
from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Sale, Card
# from .forms import StartSaleForm

# Create your views here.
# class StartSaleView(CreateView):
#     template_name = "sale/start_sale.html"
#     model = Sale
#     form_class = StartSaleForm
#     success_url = reverse_lazy('core:index')
#     success_message = "Comanda aberta!"

#     def form_valid(self, form):
#         messages.success(self.request, self.success_message)
#         sale = form.save(commit=False)
#         Card.objects.filter(pk=sale.card.pk).update(status="not_available")
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super(StartSaleView, self).get_context_data(**kwargs)
#         return context

class SaleOpenListView(ListView):
    model = Sale
    queryset = Sale.objects.filter(status='open')
    template_name = 'sale/sale_open_list.html'