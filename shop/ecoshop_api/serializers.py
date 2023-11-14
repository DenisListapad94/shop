# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import ProductApi


class ProductApiSerializer(ModelSerializer):
    class Meta:
        model = ProductApi
        fields = ['id', 'name', 'price', 'amount']
    def create(self, validated_data):
        return ProductApi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance