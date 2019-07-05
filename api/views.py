from rest_framework.viewsets import ModelViewSet
from .serializers import IngredientSerializer, RecipeSerializer
from .models import Ingredient, Recipe
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class IngredientViewSet(ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class RecipeViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    #authentication_classes = (TokenAuthentication,) ovo sta je zakomentirano promijeni
    #permission_classes = (IsAuthenticated,)


class IngredientViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsAuthenticated,)