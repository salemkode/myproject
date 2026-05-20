from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("preparing", "Preparing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    ]
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    delivery_address = models.TextField()

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}x {self.product.name}"


class Package(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="packages")
    deliverer = models.ForeignKey("delivery.Deliverer", on_delete=models.SET_NULL, null=True, blank=True)
    tracking_number = models.CharField(max_length=100, unique=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    delivered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Package {self.tracking_number}"
