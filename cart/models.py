from django.db import models
from product.models import Variation
from user.models import CustomerUser
# Create your models here.

class Cart(models.Model):
    # auto_now : thời điểm hiện tại của hệ thống(cập nhật trường mỗi lần)
    # auto_now_add : thời điểm chỉ cập nhật khi tạo 
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0)
