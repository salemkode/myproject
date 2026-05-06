from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
