from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
import decimal


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

    def total_price(self):
        return sum(cartitem.total_price() for cartitem in self.cart_item.all())
        



class CartItem(models.Model):
    # order = models.ForeignKey(Cart, on_delete=models.CASCADE , related_name = 'carts',blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE , related_name = 'cart_item',blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'cart_product')
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity
         
            