from rest_framework.routers import DefaultRouter
from .viewsets import FoodCategoryViewSet

router = DefaultRouter()
router.register('foods', FoodCategoryViewSet)
urlpatterns = router.urls
