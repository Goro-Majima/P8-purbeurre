from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    nutrigrade = models.CharField(max_length=1)
    image = models.URLField()
    url = models.URLField()
    nutrient = models.URLField(default='image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.name

class Favorites(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.User + " " + self.product