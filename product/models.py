from django.db import models
from django.contrib.auth.models import User
from category.models import Category
# Create your models here.


class Product(models.Model):
    TYPE = (("جدید", "بله"), (" ", "خیر"))
    title: models.CharField(max_length=200, verbose_name="عنوان محصول")
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


    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"