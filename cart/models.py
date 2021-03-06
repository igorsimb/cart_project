from django.db import models
from django.db.models import F


class Topping(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_added = models.BooleanField(default=False)

    def __str__(self):
        return self.name
