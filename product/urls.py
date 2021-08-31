# Imports
from django.urls import path

from product import views

# Create your urls here.
app_name = "product"

urlpatterns = [
    path('add/', views.ProductAddView.as_view(), name="add"),
    path('list/', views.ProductListView.as_view(), name="list"),
]