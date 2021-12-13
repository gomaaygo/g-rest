from django.urls import path, include
from account import views as a_views
from . import views

app_name = 'core'

urlpatterns = [
    path('', a_views.sign_in, name='signin'),
    path('home', views.IndexTemplateView.as_view(), name='index'),
]