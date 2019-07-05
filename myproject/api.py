from rest_framework.routers import DefaultRouter
from api.views import RecipeViewSet, IngredientViewSet
from rest_framework_extensions.routers import NestedRouterMixin

router = DefaultRouter()

router.register('recipes', RecipeViewSet)
router.register('ingredients', IngredientViewSet)


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()


recipes_router = router.register('recipes', RecipeViewSet)
recipes_router.register(
    'ingredients', IngredientViewSet,
    basename='recipe-ingredients',
    parents_query_lookups=['recipe'])
