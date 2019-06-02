import datetime

from django.db import models
from django.db.models.functions import Trunc
from django.core.paginator import Paginator


class TimeFilter(models.QuerySet):
    def today(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        return self.filter(date__date=now.date())

    def year(self, date: datetime.date):
        return self.filter(date__year=date.year)

    def month(self, date: datetime.date):
        return self.filter(date__year=date.year, date__month=date.month)

    def week(self, date: datetime.date):
        start = date - datetime.timedelta(days=date.weekday())  # Monday
        end = start + datetime.timedelta(days=6)  # Sunday
        return self.filter(date__date__range=[start, end])

    def day(self, date: datetime.date):
        return self.filter(date__date=date)


class Counters(models.QuerySet):
    def _counts(self, timespan: str):
        assert timespan in ["year", "month", "week", "day"]

        data = {timespan: Trunc("date", timespan, output_field=models.DateField())}

        return (
            self.annotate(**data)
            .values(timespan)
            .annotate(count=models.Count(timespan))
            .order_by(timespan)
        )

    def counts_yearly(self):
        return self._counts("year")

    def counts_monthly(self):
        return self._counts("month")

    def counts_weekly(self):
        return self._counts("week")

    def counts_daily(self):
        return self._counts("day")


class TopAggregation(models.QuerySet):
    def top_artists(self):
        items = (
            self.values("artist__name", "artist__id")
            .annotate(count=models.Count("artist__name"))
            .order_by("-count", "artist__name")
        )

        return items

    def top_albums(self):
        items = (
            self.exclude(album=None)
            .values("artist__name", "album__title", "album__id")
            .annotate(count=models.Count("album__id"))
            .order_by("-count", "artist__name", "album__title")
        )

        return items

    def top_tracks(self):
        items = (
            self.values("artist__name", "track__title", "track__id")
            .annotate(count=models.Count("track__id"))
            .order_by("-count", "artist__name", "track__title")
        )

        return items

    def top_listeners(self):
        items = (
            self.values("profile__user__username")
            .annotate(count=models.Count("profile__user__username"))
            .order_by("-count", "profile__user__username")
        )

        return items


class ScrobbleQuerySet(TimeFilter, TopAggregation, Counters):
    def paginated(self):
        return Paginator(self, 10)

    def recent_list(self):
        return self.values("artist__name", "track__title", "date")
