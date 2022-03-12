from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.


class ProductListView(ListView):
    template_name = "product/product-list.html"
    model = Product
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.product_are_active()


