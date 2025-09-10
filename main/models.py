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
        thumbnail="https://images.unsplash.com/photo-1637437757614-6491c8e915b5?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8c3BvcnQlMjBzaG9lc3xlbnwwfHwwfHx8MA%3D%3D",
        category="FOOTWEAR",
        stock=15,
        is_featured=True,
    ),
    Product(
        id=uuid.uuid4(),
        name="Pro Team Jersey",
        price=85,
        description="A breathable and lightweight jersey for professional cyclists.",
        thumbnail="https://static.vecteezy.com/system/resources/previews/024/818/573/non_2x/sports-jersey-and-t-shirt-template-sports-jersey-design-sports-design-for-football-racing-gaming-jersey-with-front-back-view-and-pattern-free-vector.jpg",
        category="JERSEY",
        stock=25,
        is_featured=True,
    ),
    Product(
        id=uuid.uuid4(),
        name="Aero Shorts",
        price=60,
        description="Aerodynamic shorts designed for maximum comfort and speed.",
        thumbnail="data:image/jpeg;base64,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",
        category="SHORTS",
        stock=30,
        is_featured=False,
    ),
    Product(
        id=uuid.uuid4(),
        name="Trail Blazer X",
        price=150,
        description="Rugged trail running shoes for the toughest terrains.",
        thumbnail="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3GjTZtXHZoq0Rq9tv4L0OHXak8r2f0ZYDyw&s",
        category="FOOTWEAR",
        stock=10,
        is_featured=False,
    ),
]

