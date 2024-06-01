from rest_framework import serializers
from book.models import Book
from mobile.models import Mobile
from clothes.models import Clothes

class SearchResultSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    type = serializers.CharField()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price']

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = ['id', 'model_name', 'description', 'price']

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['id', 'name', 'size', 'price']
