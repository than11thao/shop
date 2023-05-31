from django.db import models
from user.models import CustomerUser
from cart.models import Cart 
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shopping_address = models.CharField(max_length=255, default='')
    order_description = models.TextField(default='')
    is_complated = models.BooleanField(default=False)