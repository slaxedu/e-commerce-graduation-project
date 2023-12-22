from django.db import models
from account.models import CustomUser
from items.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])

class Address(models.Model):
    address = models.CharField(max_length=200)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # product = models.ForeignKey(OrderItems, on_delete=models.CASCADE)
    total_price = models.FloatField()
    order_date = models.DateField()
    shoping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_status = models.BooleanField(default=False)
    

class OrderItems(models.Model):
    order = models.ForeignKey(Order, null=True ,on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    

