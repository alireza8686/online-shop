from django.contrib import admin
from .models import AboutUs, OurTeam
# Register your models here.


admin.site.register(AboutUs)


@admin.register(OurTeam)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("full_name",)
    search_fields = ("full_name",)