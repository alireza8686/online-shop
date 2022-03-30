from itertools import count
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.


@login_required(login_url="login")
def create_order(request,product_id):
    card = Card.objects.filter(user=request.user, is_paid=False).first()
    if card is None:
        card = Card.objects.create(user=request.user , is_paid=False)
        card.save()
    id = product_id
    product = Product.objects.get(id=id)
    try:
        order = Order.objects.get(card=card,product=product,price = product.price)
    except:
        order = Order.objects.create(card=card,product=product,price = product.price,count=0)
        order.count += 1
        order.save()
    order = Order.objects.filter(card=card)
    return redirect('orders')


@login_required(login_url="login")
def order(request):
    card = Card.objects.get(user=request.user)
    orders = Order.objects.filter(card=card)
    context = {
        'orders' : orders
    }
    return render(request,'order/card.html',context)


def delete_order(request,id):
    order = Order.objects.filter(id=id)
    order.delete()
    return redirect('orders')
