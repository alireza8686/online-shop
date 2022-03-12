from operator import truediv
from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from django.urls import reverse
# Create your models here.


class ProductManager(models.Manager):
    def product_are_active(self):
        return self.get_queryset().filter(active=True)

class Product(models.Model):
    TYPE = (("جدید", "بله"), (" ", "خیر"))
    title = models.CharField(max_length=200, verbose_name="عنوان محصول",default="")
    description = models.TextField(verbose_name="توضیحات محصول")
    price = models.IntegerField(default="1000", blank=True, null=True, verbose_name="قیمت")
    product_size = models.CharField(max_length=500, verbose_name="سایز محصول")
    color = models.CharField(max_length=200, verbose_name="رنگ", blank=True, null=True)
    image = models.ImageField(upload_to="products", blank=True, null=True, verbose_name="تصویر محصول")
    brand = models.CharField(max_length=200, verbose_name="برند")
    new_type = models.CharField(max_length=200, choices=TYPE, default="no", verbose_name="جدید")
    special = models.BooleanField(default=False, verbose_name="محصول ویژه")
    categories = models.ManyToManyField(Category, verbose_name="دسته بندی ها")
    active = models.BooleanField(default=False, verbose_name="موجود / ناموجود")
    view = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    #manager
    objects = ProductManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})
    


class ProductComment(models.Model):
    product = models.ForeignKey(Product, verbose_name="محصول", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    text = models.TextField(verbose_name="متن نظر")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده / نشده")

    class Meta:
        verbose_name = "نظر کاربران"
        verbose_name_plural = "نطرات کاربران درباره محصولات"

    def __str__(self):
        return self.full_name