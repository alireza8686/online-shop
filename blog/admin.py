from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Blog)


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_read")
    list_editable = ("is_read",)
    list_filter = ("is_read",)
    search_fields = ("full_name",)

