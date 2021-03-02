from rest_framework import serializers
from app.models_.Product import Category, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product_name', )


