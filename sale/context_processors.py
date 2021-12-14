# Imports
import json
from datetime import date

from django.db.models import Sum

from sale.models import Sale, Card, ItemSale

today = date.today()

def get_number_sales(request):
    return {
        "n_sales": Sale.objects.filter(sale_date__year=today.year,
        sale_date__month=today.month,
        sale_date__day=today.day).count()
    }

def get_total_sales(request):
    return {
        "t_sales": Sale.objects.filter(sale_date__year=today.year,
        sale_date__month=today.month,
        sale_date__day=today.day).aggregate(total_v=Sum('total'))
    }

def get_number_card(request):
    return {
        "n_cards": Card.objects.filter(status="available").count()
    }

def get_number_items(request):
    return {
        "items": ItemSale.objects.filter(sale__sale_date__year=today.year, 
        sale__sale_date__month=today.month,
        sale__sale_date__day=today.day).aggregate(quantity=Sum('quantity'))
    }
