from django.urls import path
from .views import create_order

urlpatterns = [
    path('orders/<int:product_id>/',create_order,name='orders'),
]
