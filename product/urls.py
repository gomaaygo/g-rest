# Imports
from django.urls import path

from product import views

# Create your urls here.
app_name = "product"

urlpatterns = [
    path('add/', views.ProductAddView.as_view(), name="add"),
    path('list/', views.ProductListView.as_view(), name="list"),
    path('<int:pk>/edit/', views.EditProductView.as_view(), name='edit'),
    path('input/stock/', views.InputOfProductStockView.as_view(), name="input-product-stock"),
    path('output/stock/', views.OutputOfProductStockView.as_view(), name="output-product-stock"),
    path('stock/list/', views.StockListView.as_view(), name="stock-list"),
    path('category/add/', views.CategoryAddView.as_view(), name="category-add"),
    path('input/stock/list/', views.InputOfProductListView.as_view(), name="input-of-product-list"),
    path('output/stock/list/', views.OutputOfProductListView.as_view(), name="output-of-product-list"),
    path('category/list/', views.CategoryListView.as_view(), name="category-list"),
]