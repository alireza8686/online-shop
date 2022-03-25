from django.shortcuts import render
from settings.models import SiteInformation
from sliders.models import Slider
from product.models import Product
from blog.models import Blog
# Create your views here.


def home_page(request):
    sliders = Slider.objects.all()
    setting = SiteInformation.objects.get(id=1)
    special_product = Product.objects.filter(special=True).all()[:3]
    new_product = Product.objects.order_by("-id").all()[:4]
    product_by_view = Product.objects.order_by("-view").all()[:4]
    lasted_blog = Blog.objects.order_by("-id").all()[:2]
    context = {
        'setting' : setting,
        'sliders' : sliders,
        'specials' : special_product,
        'news' : new_product,
        'bests' : product_by_view,
        'last_blogs' : lasted_blog,
    }
    return render(request,'home/home.html',context)