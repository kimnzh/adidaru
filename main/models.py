import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("FOOTWEAR", "Footwear"),
        ("JERSEY", "Jersey"),
        ("SHORTS", "Shorts"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=63)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    stock = models.IntegerField()
    is_featured = models.BooleanField()

    def __str__(self):
        return f"{self.name} ({self.category})"
