from django.db import models
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    class ProductStatus(models.TextChoices):
        IN_STOCK = "In Stock"
        OUT_OF_STOCK = "Out of Stock"

    name = models.CharField(max_length=15, unique=True)
    status = models.CharField(
        max_length=30, choices=ProductStatus.choices, default=ProductStatus.IN_STOCK
    )
    last_updated = models.DateTimeField(default=now, editable=True)

    def __str__(self) -> str:
        return self.name
