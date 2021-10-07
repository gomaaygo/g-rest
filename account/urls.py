from django.urls import path, include
from . import views 

app_name = 'account'

urlpatterns = [ 
    path('login/', views.sign_in, name='signin'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.AccountCreateView.as_view(), name='register'), 
]