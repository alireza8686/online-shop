from django.urls import path
from .views import create_order

urlpatterns = [
    path('orders/',create_order,name='orders'),
]
