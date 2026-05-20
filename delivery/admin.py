from django.contrib import admin

from delivery.models import Deliverer


@admin.register(Deliverer)
class DelivererAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "is_available")
    list_editable = ["is_available"]
