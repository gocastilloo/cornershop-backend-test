"""Django serializer for each model"""
from rest_framework import serializers
from .utils.models import Ingredients


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients

