from django.contrib import admin

from products.models import Order, OrderItem, Package, Product


admin.site.register(Product)
admin.site.register(OrderItem)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "created_at")
    list_filter = ("status",)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("tracking_number", "order", "deliverer", "weight", "delivered_at")
