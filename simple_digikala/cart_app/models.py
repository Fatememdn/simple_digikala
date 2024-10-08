from django.db import models
from product_app.models import Product
from accounts.models import Costumer, Seller

class Cart(models.Model):
    buyer = models.ForeignKey(Costumer, on_delete = models.CASCADE,blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete= models.CASCADE,blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    is_finalized = models.BooleanField(default=True, blank=True, null=True)
    bill = models.FloatField(blank=True, null=True)
    

    def __str__(self) -> str:
        return f'{self.buyer}, {self.seller}, {self.code}'
    
class Cart_item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, help_text='this product', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    num = models.IntegerField(blank= True, null=True)

    def __str__(self) -> str:
        return f'{self.cart}, {self.product}'
