from django.db import models


class Deliverer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
