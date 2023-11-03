from django.contrib import admin
from django.contrib.admin import AdminSite, ModelAdmin
from .models import Config
from main.admin import magasagyas_admin_site


class ConfigsAdminModel(admin.ModelAdmin):
    list_display = ("id","created_at")
    list_per_page = 10
    ordering = ("-id",)


admin.site.register(Config,ConfigsAdminModel)
