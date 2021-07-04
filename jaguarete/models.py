from django.db import models
from django.db.models import Sum
from django.conf import settings
import os


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30, default="Categoria")
    description = models.CharField(max_length=300)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="products")
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        for field_name in ['title']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Product, self).save(*args, **kwargs)

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products_list = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return "Carrito de " + self.user.username  
    
    @property
    def total_price(self):
        "Returns the person's full name."
        total = 0
        for item in self.products_list.all():
            total += item.price
        return total
    

