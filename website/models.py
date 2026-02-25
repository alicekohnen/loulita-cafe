from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ("coffee", "Coffee"),
        ("pastry", "Pastry"),
        ("seasonal", "Seasonal"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    ingredients = models.TextField()
    allergens = models.TextField(blank=True)

    def __str__(self):
        return self.name