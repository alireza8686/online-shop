from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.


@login_required(login_url="login")
def create_order(request):
    order_form = OrderForm(request.POST)

    if order_form.is_valid():
        card = Card.objects.filter(user=request.user, is_paid=False).first()
        if card is None:
            card = Card.objects.create(user=request.user , is_paid=False)
            card.save()
        product_id = order_form.cleaned_data.get("product_id")
        count = order_form.cleaned_data.get("count")
        if count <= 0:
            count = 1

        product = Product.objects.get(id=product_id)
        order = Order.objects.create(card=card,product=product,price = product.price , count = count)
        
        context = {
            'order' : order,
            'card' : card,
        }
        return render(request,'order/orders.html',context)
    return render(request,'order/orders.html')