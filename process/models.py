from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
import datetime

now = datetime.datetime.now()
User = get_user_model()
class Cart(models.Model):
    STATUS_PAID = [
        ('NP','Not-Paid'),
        ('P','Paid')
    ]
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')
    status = models.CharField(choices= STATUS_PAID,max_length=2 , null=True, blank=True)
    ordered = models.BooleanField(default=False)
    date_paid = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.user.username





class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE , related_name = 'cart_item',blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'cart_product')
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.product.title

