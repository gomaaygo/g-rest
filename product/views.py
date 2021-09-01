# Imports
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib import messages

from .models import Product, InputOfProduct, OutputOfProduct
from .forms import ProductForm, InputOfProductForm, OutputOfProductForm

# Create your views here.
class ProductAddView(CreateView):
    template_name = "product/product_add.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:add')
    success_message = "Produto cadastrado com sucesso!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        product = form.save(commit=False)
        product.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductAddView, self).get_context_data(**kwargs)
        return context


class ProductListView(ListView):
    model = Product


class InputOfProductStockView(CreateView):
    template_name = "product/input_of_product.html"
    model = InputOfProduct
    form_class = InputOfProductForm
    success_url = reverse_lazy('product:input-product-stock')
    success_message = "Produto adicionado ao estoque!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        input_product = form.save(commit=False)
        # input_product.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(InputOfProductStockView, self).get_context_data(**kwargs)
        return context


class OutputOfProductStockView(CreateView):
    template_name = "product/output_of_product.html"
    model = OutputOfProduct
    form_class = OutputOfProductForm
    success_url = reverse_lazy('product:output-product-stock')
    success_message = "Produto retirado do estoque!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        input_product = form.save(commit=False)
        # input_product.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OutputOfProductStockView, self).get_context_data(**kwargs)
        return context