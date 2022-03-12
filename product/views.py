from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView

from product.forms import ProductCommentForm
from .models import *
# Create your views here.


class ProductListView(ListView):
    template_name = "product/product-list.html"
    model = Product
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.product_are_active()

    


def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    comment_form = ProductCommentForm(request.POST)
    comments = ProductComment.objects.filter(product=product, is_read=True)
    product.view += 1
    product.save()

    related_product: Product = Product.objects.get_queryset().filter(categories__product=product).all()

    if comment_form.is_valid():
        comment = ProductComment.objects.create(
            product = product,
            full_name = comment_form.cleaned_data['full_name'],
            email = comment_form.cleaned_data['email'],
            text = comment_form.cleaned_data['text'],
        )
        comment.save()
    else:
        comment_form = ProductCommentForm()
    context = {
        'product' : product,
        'comment_form' : comment_form,
        'comments':comments,
        'related_product' : related_product,
    }
    return render(request,'product/product-detail.html',context)


class SpecialProducts(ListView):
    template_name = "product/product-list.html"
    model = Product
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.filter(special=True, active=True).all()

class ProductNew(ListView):
    template_name = "product/product-list.html"
    model = Product
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.order_by("-id").all()



class ProductMostPopular(ListView):
    template_name = "product/product-list.html"
    model = Product
    paginate_by = 4

    def get_queryset(self):
        return Product.objects.order_by("-view").all()
