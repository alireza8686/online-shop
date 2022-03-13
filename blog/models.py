from django.db import models
from django.urls import reverse
# Create your models here.


class BlogManager(models.Manager):
    def get_published(self):
        return self.get_queryset().filter(is_published=True)

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توصیحات")
    author = models.CharField(max_length=200, verbose_name="نام نویسنده")
    image = models.ImageField(upload_to="blog", verbose_name="تصویر", blank=True, null=True)
    time = models.DateTimeField(verbose_name="زمان انتشار", blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name="منتشر شود / نشود")
    view = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    objects = BlogManager()

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-detail", args={self.pk})
    
    
    
    
class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name="وبلاگ", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    text = models.TextField(verbose_name="متن نظر")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده / نشده")

    class Meta:
        verbose_name = "نظرات"
        verbose_name_plural = "نطرات کاربران "

    def __str__(self):
        return self.full_name