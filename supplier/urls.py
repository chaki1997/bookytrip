from django.urls import path
from . import views

app_name = "supplier"

urlpatterns = [
    path('payments', views.supplier_payment, 'payment'),
]
