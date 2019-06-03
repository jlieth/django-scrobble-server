from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

CHART_CATEGORIES = (("artists", "artists"), ("albums", "albums"), ("tracks", "tracks"))

TIMESPANS = (
    ("day", "day"),
    ("week", "week"),
    ("month", "month"),
    ("year", "year"),
    ("all", "all"),
)


class ChartsCache(models.Model):
    # fields for generic object relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    obj = GenericForeignKey("content_type", "object_id")

    category = models.CharField(max_length=7, choices=CHART_CATEGORIES)
    timespan = models.CharField(max_length=5, choices=TIMESPANS)
    date = models.DateField()
    toplist = models.TextField()
    total_listens = models.IntegerField()
    max_listen_count = models.IntegerField()

    class Meta:
        indexes = [models.Index(fields=["category", "timespan", "date"])]
        unique_together = [
            ["content_type", "object_id", "category", "timespan", "date"]
        ]
