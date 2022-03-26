from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.


@login_required(login_url="login")
def user_order(request):
    order_form = OrderForm(request.POST)

    if order_form.is_valid():
        order = Card.objects.filter(user=request.user, is_paid=False).first()
        if order is None:
            order = Card.objects.create(user=request.user , is_paid=False)

        product = order_form.cleaned_data.get("product")
        count = order_form.cleaned_data.get("count")
        if count <= 0:
            count = 1

        product = Product.objects.get(product=product)

        order.orderdetail_set.create(product=product.id, count=count, price=product.price)
        return redirect(f"products/{product.id}/{product.title.replace(' ', '-')}")
    return redirect("/")