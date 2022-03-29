from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده / نشده")
    paid_date = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ پرداخت")

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید کاربران"

    def __str__(self):
        return self.user.get_full_name()

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount
    
    
class Order(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name="سبد خرید")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    price = models.IntegerField(verbose_name="قیمت")
    count = models.IntegerField(verbose_name="تعداد")

    class Meta:
        verbose_name = "جزییات سبد خرید"
        verbose_name_plural = "اطلاعات سبد های خرید کاربران"

    def __str__(self):
        return self.product.title

    def price_complete(self):
        return self.price * self.count