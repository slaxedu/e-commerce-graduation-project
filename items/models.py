from django.db import models
from account.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.indexes import GinIndex

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='image/category', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/brand', blank=True, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=4000, null=True, blank=True)
    image = models.ImageField(upload_to='image/product', blank=True, null=True)
    quantity_in_stock = models.IntegerField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=True)
    is_solid = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=255)
    # class Meta:
    #     indexes = [GinIndex(fields=['name'])]
    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.CharField(max_length=4000, null=True, blank=True)
class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    crated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment

class Variation(models.Model):
    product_id = models.ForeignKey(Product,default=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name


class VariationOption(models.Model):
    variation_id = models.ForeignKey(Variation, on_delete=models.CASCADE)
    value = models.CharField(max_length=150)
    def __str__(self):
        return self.value