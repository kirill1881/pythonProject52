from rest_framework import serializers
from .models import ItemModel


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=255)
    product_price = serializers.FloatField()
    product_weight = serializers.FloatField()

    class Meta:
        model = ItemModel
        fields = '__all__'
