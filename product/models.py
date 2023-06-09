from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(default='' , max_length=255)
    slug = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(default='' , max_length=255)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    product_img = models.CharField(default='', max_length=255)

class Variation(models.Model):
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    title = models.CharField(default='' , max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
