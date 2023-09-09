from django.contrib import admin

from .models import Shop, SalesCampaign, Product

class ShopAdmin(admin.ModelAdmin):
    fields = ["name", "is_point_extra_service"]


class SalesCampaignAdmin(admin.ModelAdmin):
    fields = ["name", "start_date", "end_date"]

class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "charge", "shop"]


admin.site.register(Shop, ShopAdmin)
admin.site.register(SalesCampaign, SalesCampaignAdmin)
admin.site.register(Product, ProductAdmin)

