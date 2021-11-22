# Imports
from django.urls import path

from sale import views

# Create your urls here.
app_name = "sale"

urlpatterns = [
    path('<int:pk>/add/item', views.add_item_sale, name="add-item-sale"),
    path('list/', views.SaleOpenListView.as_view(), name="sale-open-list"),
    path('<int:pk>/', views.SaleDetailView.as_view(), name='sale-detail'),
    path('new', views.new_sale, name='new-sale'),
    path('<int:pk>/close', views.close_sale, name='sale-close'),
]