from django.db import models


class ItemModel(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_weight = models.FloatField()
