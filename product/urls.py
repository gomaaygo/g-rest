# Imports
from django.urls import path

from product import views

# Create your urls here.
app_name = "product"

urlpatterns = [
    path('add/', views.ProductAddView.as_view(), name="add"),
    path('list/', views.ProductListView.as_view(), name="list"),
    path('<int:pk>/edit/', views.EditProductView.as_view(), name='edit'),
    path('input/stock/', views.EntryOfSaleProductIntoStockView.as_view(), name="input-product-stock"),
    path('output/stock/', views.OutputOfProductStockView.as_view(), name="output-product-stock"),
    path('stock/list/', views.StockListView.as_view(), name="stock-list"),
    path('deposit/list/', views.DepositListView.as_view(), name="deposit-list"),
    path('category/add/', views.CategoryAddView.as_view(), name="category-add"),
    path('input/stock/list/', views.InputOfProductSaleListView.as_view(), name="input-of-product-sale-list"),
    path('output/stock/list/', views.OutputOfProductSaleListView.as_view(), name="output-of-product-sale-list"),
    path('input/deposit/list/', views.InputOfProductConsumptionListView.as_view(), name="input-of-product-consumption-list"),
    path('output/deposit/list/', views.OutputOfProductConsumptionListView.as_view(), name="output-of-product-consumption-list"),
    path('category/list/', views.CategoryListView.as_view(), name="category-list"),
    path('category/<int:pk>/edit/', views.EditCategoryView.as_view(), name='category-edit'),
]