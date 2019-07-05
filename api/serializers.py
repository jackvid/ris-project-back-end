from rest_framework.serializers import ModelSerializer
from .models import Ingredient, Recipe


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description', 'imagePath')


class IngredientSerializer(ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'recipe', 'name', 'amount')
