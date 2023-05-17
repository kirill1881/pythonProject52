from rest_framework import serializers
from .models import ItemModel
from .helpers import OrderToShow



class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=255)
    product_price = serializers.FloatField()
    product_weight = serializers.FloatField()

    class Meta:
        model = ItemModel
        fields = '__all__'

class ItemModelSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=255)
    product_price = serializers.FloatField()
    product_weight = serializers.FloatField()

    class Meta:
        model = ItemModel
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    if_get = serializers.BooleanField()

    class Meta:
        model = ItemModel
        fields = '__all__'

class OrderToShowSerializer(serializers.SerializerMetaclass):
    name = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    number = serializers.CharField(max_length=255)
    adress =serializers.CharField(max_length=255)
    item_name = serializers.CharField(max_length=255)

    class Meta:
        model = OrderToShow
        fields = '__all__'
