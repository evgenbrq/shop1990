from django.contrib import admin

from store.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ["name"]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)