from django.urls import path, include
from . import views 

app_name = 'account'

urlpatterns = [ 
    path('login/', views.sing_up, name='singup'),
]