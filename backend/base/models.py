from django.db import models
from datetime import datetime
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=250, blank=False, null=False)
    production_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.product_name