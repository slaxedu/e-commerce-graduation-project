from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Product)
# admin.site.register(models.product_item)
admin.site.register(models.Variation)
admin.site.register(models.VariationOption)