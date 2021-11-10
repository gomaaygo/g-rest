# Imports
from django.urls import path

from sale import views

# Create your urls here.
app_name = "sale"

urlpatterns = [
    path('list/', views.SaleOpenListView.as_view(), name="sale-open-list"),
    path('<int:pk>/', views.SaleDetailView.as_view(), name='sale-detail'),
]