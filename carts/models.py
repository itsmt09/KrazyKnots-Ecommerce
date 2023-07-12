from django.db import models

from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(blank=True, max_length=250)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.cart_id)
    

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def subtotal(self):
        return (self.product.price * self.quantity)

    def __str__(self):
        return str(self.product)
    