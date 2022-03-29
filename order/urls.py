from django.urls import path
from .views import create_order, order

urlpatterns = [
    path('create-order/<int:product_id>/',create_order,name='create-order'),
    path('orders/',order,name='orders'),
]
