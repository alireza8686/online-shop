from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Product)




@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_read")
    list_editable = ("is_read",)
    list_filter = ("is_read",)
    search_fields = ("full_name",)