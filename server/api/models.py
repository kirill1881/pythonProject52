from django.db import models


class ItemModel(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_weight = models.FloatField()


class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True)

class Order(models.Model):
    item_id = models.IntegerField()
    user_id = models.IntegerField()
    if_get = models.BooleanField()
