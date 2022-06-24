# Imports
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib import messages
from account.permissions import GroupRequiredMixin
from django.views.generic import UpdateView

from .models import Product, Stock, InputOfProduct, OutputOfProduct, Category
from .forms import (ProductForm, EntryOfSaleProductIntoStockForm,
                    EntryOfConsumptionProductIntoStockForm,
                    OutputOfProductForm, CategoryForm)

# Create your views here.
class ProductAddView(GroupRequiredMixin, CreateView):
    group_required = [u'Gerente', u'Caixa']
    template_name = "product/product_add.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:list')
    success_message = "Produto cadastrado com sucesso!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        product = form.save(commit=False)
        product.save()

        stock = Stock.objects.create(
            product=Product.objects.get(pk=product.pk),
            quantity_min=form.cleaned_data['quantity_min'],
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductAddView, self).get_context_data(**kwargs)
        return context


class ProductListView(ListView):
    model = Product


class EntryOfSaleProductIntoStockView(GroupRequiredMixin, CreateView):
    group_required = [u'Gerente', u'Caixa']
    template_name = "product/input_of_product.html"
    model = InputOfProduct
    form_class = EntryOfSaleProductIntoStockForm
    success_url = reverse_lazy('product:input-product-stock')
    success_message = "Produto adicionado ao estoque!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        input_product = form.save(commit=False)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EntryOfSaleProductIntoStockView, self).get_context_data(**kwargs)
        context['type_form'] = "Estoque"
        return context
    

class EntryOfConsumptionProductIntoStockView(GroupRequiredMixin, CreateView):
    group_required = [u'Gerente', u'Caixa']
    template_name = "product/input_of_product.html"
    model = InputOfProduct
    form_class = EntryOfConsumptionProductIntoStockForm
    success_url = reverse_lazy('product:input-product-stock')
    success_message = "Produto adicionado ao depósito!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        input_product = form.save(commit=False)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EntryOfConsumptionProductIntoStockView, self).get_context_data(**kwargs)
        context['type_form'] = "Depósito"
        return context


class OutputOfConsumptionProductIntoStockView(GroupRequiredMixin, CreateView):
    group_required = [u'Gerente', u'Caixa']
    template_name = "product/output_of_product.html"
    model = OutputOfProduct
    form_class = OutputOfProductForm
    success_url = reverse_lazy('product:output-product-deposit')
    success_message = "Produto retirado do depósito!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        input_product = form.save(commit=False)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OutputOfConsumptionProductIntoStockView, self).get_context_data(**kwargs)
        return context


class StockListView(GroupRequiredMixin, ListView):
    group_required = [u'Gerente', u'Caixa'] 
    model = Stock
    queryset = Stock.objects.filter(product__type_product="sale")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_list'] = "Estoque"
        return context
    

class DepositListView(GroupRequiredMixin, ListView):
    group_required = [u'Gerente', u'Caixa'] 
    model = Stock
    queryset = Stock.objects.filter(product__type_product="consumption")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_list'] = "Depósito"
        return context


class CategoryAddView(GroupRequiredMixin, CreateView):
    group_required = [u'Gerente', u'Caixa']
    template_name = "product/category_add.html"
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('product:add')
    success_message = "Categoria cadastrada com sucesso!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        category = form.save(commit=False)
        category.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CategoryAddView, self).get_context_data(**kwargs)
        return context


class InputOfProductSaleListView(GroupRequiredMixin, ListView):
    group_required = [u'Gerente', u'Caixa']
    model = InputOfProduct
    queryset = InputOfProduct.objects.filter(product__type_product="sale").order_by("-entry_date")


class OutputOfProductSaleListView(GroupRequiredMixin, ListView):
    group_required = [u'Gerente', u'Caixa']
    model = OutputOfProduct
    queryset = OutputOfProduct.objects.filter(product__type_product="sale").order_by("-departure_date")
    
    
class InputOfProductConsumptionListView(GroupRequiredMixin, ListView):
    group_required = [u'Gerente', u'Caixa']
    model = InputOfProduct
    queryset = InputOfProduct.objects.filter(product__type_product="consumption").order_by("-entry_date")


class OutputOfProductConsumptionListView(GroupRequiredMixin, ListView):
    group_required = [u'Gerente', u'Caixa']
    model = OutputOfProduct
    queryset = OutputOfProduct.objects.filter(product__type_product="consumption").order_by("-departure_date")


class EditProductView(GroupRequiredMixin, UpdateView):
    group_required = [u'Gerente', u'Caixa']
    model = Product
    template_name = 'product/edit_product.html'
    form_class = ProductForm

    def get_success_url(self):
        messages.success(self.request, "Produto atualizado com sucesso!")  
        return reverse('product:list')


class CategoryListView(GroupRequiredMixin, ListView):
    group_required = [u'Gerente', u'Caixa'] 
    model = Category


class EditCategoryView(GroupRequiredMixin, UpdateView):
    group_required = [u'Gerente', u'Caixa']
    model = Category
    template_name = 'product/edit_category.html'
    form_class = CategoryForm

    def get_success_url(self):
        messages.success(self.request, "Categoria atualizada com sucesso!")  
        return reverse('product:category-list')