from rest_framework import serializers
from task3_10.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title", "price", "marja", "package_code")
