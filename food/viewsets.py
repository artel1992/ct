from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from food.models import Food, FoodCategory
from .serializers import FoodSerializer
from .serializers import FoodCategorySerializer


class FoodViewSet(ModelViewSet):
    queryset = Food.publish_only.all()
    serializer_class = FoodSerializer


class FoodCategoryViewSet(ModelViewSet):
    queryset = FoodCategory.objects.prefetch_related(
        Prefetch('food', queryset=Food.publish_only.all()),
        Prefetch('food__additional')) \
        .filter(food__is_publish=True).distinct()
    serializer_class = FoodCategorySerializer
