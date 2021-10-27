# Imports
from django.urls import path

from sale import views

# Create your urls here.
app_name = "sale"

urlpatterns = [
    # path('start/', views.StartSaleView.as_view(), name="start-sale"),
    path('list/', views.SaleOpenListView.as_view(), name="sale-open-list"),
]