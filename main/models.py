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
    
PRODUCTS = [
    Product(
        id=uuid.uuid4(),
        name="Flyer V-2",
        price=120,
        description="High-performance running shoes with advanced cushioning.",
        thumbnail="https://placehold.co/600x400/222/fff?text=Flyer+V-2",
        category="FOOTWEAR",
        stock=15,
        is_featured=True,
    ),
    Product(
        id=uuid.uuid4(),
        name="Pro Team Jersey",
        price=85,
        description="A breathable and lightweight jersey for professional cyclists.",
        thumbnail="https://placehold.co/600x400/222/fff?text=Pro+Jersey",
        category="JERSEY",
        stock=25,
        is_featured=True,
    ),
    Product(
        id=uuid.uuid4(),
        name="Aero Shorts",
        price=60,
        description="Aerodynamic shorts designed for maximum comfort and speed.",
        thumbnail="https://placehold.co/600x400/222/fff?text=Aero+Shorts",
        category="SHORTS",
        stock=30,
        is_featured=False,
    ),
    Product(
        id=uuid.uuid4(),
        name="Trail Blazer X",
        price=150,
        description="Rugged trail running shoes for the toughest terrains.",
        thumbnail="https://placehold.co/600x400/222/fff?text=Trail+Blazer",
        category="FOOTWEAR",
        stock=10,
        is_featured=False,
    ),
]

