from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class CustomUser(AbstractUser):
    store = models.CharField(max_length=250, blank=True, null=True)


class Product(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    product_name = models.CharField(max_length=250, blank=False, null=False)
    production_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.product_name
