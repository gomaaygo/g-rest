from django.urls import path, include
from . import views 

app_name = 'account'

urlpatterns = [ 
    path('', views.sign_in, name='signin'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.AccountCreateView.as_view(), name='register'),
    path('<int:pk>/edit/', views.EditAccountView.as_view(), name='edit'),
    path('newpass/', views.NewPasswordView.as_view(), name='new-password'),
    path('<int:pk>/profile/', views.AccountDetailView.as_view(), name='account-detail'),
    path('list/', views.AccountListView.as_view(), name="list"),
    path('<int:pk>/permission', views.system_permission, name='permission'), 
]