from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import Product
from .forms import ProductForm

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