from django.db import models


class FoodPublishedOnlyManager(models.Manager):
    def get_queryset(self):
        return super(FoodPublishedOnlyManager, self).get_queryset().filter(is_publish=True)
