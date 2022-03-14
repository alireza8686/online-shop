from django.db import models


# Create your models here.

class SiteInformation(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان سایت")
    address = models.CharField(max_length=500, verbose_name="آدرس", blank=True, null=True)
    phone = models.CharField(max_length=25, verbose_name="شماره تماس", blank=True, null=True)
    email = models.EmailField(verbose_name="ایمیل", blank=True, null=True)
    logo = models.ImageField(upload_to="logo", verbose_name="لوگوی سایت(48*48)", blank=True, null=True)
    description = models.TextField(verbose_name="توضیحات درباره سایت")

    class Meta:
        verbose_name = "تنظیم سایت"
        verbose_name_plural = "تنظیم اطلاعات سایت"

    def __str__(self):
        return self.title


