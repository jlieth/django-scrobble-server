import datetime

from freezegun import freeze_time
from django.test import TestCase

from scrobble_server.core.models.submissions import Scrobble
from tests import data


class TimeFilterTests(TestCase):
    """
    Tests for scrobble_server.core.querysets.TimeFilter

    Testing for the filtering methods (year, month, week, day) is pretty
    straight-forward. A fixture with known scrobble data is loaded.
    Scrobble queryset is filtered using the method that is being tested and
    ordered by date. The queryset's count() method is being used to check the
    scrobble counts against expected values. First and last items' dates are
    checked to make sure that all items in the queryset are within the
    expected time range.

    For (year, month, week) filters, the full queryset is again filtered with
    a different day from the time period as "anchorpoint". The resulting
    querysets should be identical. (That is, selecting year with anchor point
    2009-12-31 should yield the same queryset as with anchor point 2009-01-01).
    This test is obviously not applicable to the day filter because the time
    period is only one day so there can be only one anchor point.

    TimeFilter.today is tested using freezegun. The date is artificially
    frozen to 2009-05-17. The resulting queryset for the today method is
    compared to the queryset resulting from filtering for the date directly.
    The querysets should be identical.
    """

    fixtures = ["user_and_profile", "charts_testdata"]

    def test_year(self):
        """Tests scrobble_server.core.querysets.TimeFilter.year"""
        d = datetime.date(2009, 5, 27)
        qs = Scrobble.objects.year(d).order_by("date")

        # check scrobble count
        self.assertEqual(qs.count(), 546)

        # check start and end dates of date range
        first = qs.first().date
        last = qs.last().date
        self.assertGreaterEqual(
            first, datetime.datetime(2009, 1, 1, tzinfo=datetime.timezone.utc)
        )
        self.assertLess(
            last, datetime.datetime(2010, 1, 1, tzinfo=datetime.timezone.utc)
        )

        # check queryset with a different anchor point from same time period
        d2 = datetime.date(2009, 1, 1)
        qs2 = Scrobble.objects.year(d2).order_by("date")
        self.assertEqual(list(qs), list(qs2))

    def test_month(self):
        """Tests scrobble_server.core.querysets.TimeFilter.year"""
        d = datetime.date(2009, 5, 27)
        qs = Scrobble.objects.month(d).order_by("date")

        # check scrobble count
        self.assertEqual(qs.count(), 273)

        # check start and end dates of date range
        first = qs.first().date
        last = qs.last().date
        self.assertGreaterEqual(
            first, datetime.datetime(2009, 5, 1, tzinfo=datetime.timezone.utc)
        )
        self.assertLess(
            last, datetime.datetime(2010, 6, 1, tzinfo=datetime.timezone.utc)
        )

        # check queryset with a different anchor point from same time period
        d2 = datetime.date(2009, 5, 1)
        qs2 = Scrobble.objects.month(d2).order_by("date")
        self.assertEqual(list(qs), list(qs2))

    def test_week(self):
        """Tests scrobble_server.core.querysets.TimeFilter.week"""
        d = datetime.date(2009, 5, 27)
        qs = Scrobble.objects.week(d).order_by("date")

        # check scrobble count
        self.assertEqual(qs.count(), 34)

        # check start and end dates of date range
        first = qs.first().date
        last = qs.last().date
        self.assertGreaterEqual(
            first, datetime.datetime(2009, 5, 25, tzinfo=datetime.timezone.utc)
        )
        self.assertLess(
            last, datetime.datetime(2010, 6, 1, tzinfo=datetime.timezone.utc)
        )

        # check queryset with a different anchor point from same time period
        d2 = datetime.date(2009, 5, 31)
        qs2 = Scrobble.objects.week(d2).order_by("date")
        self.assertEqual(list(qs), list(qs2))

    def test_day(self):
        """Tests scrobble_server.core.querysets.TimeFilter.day"""
        d = datetime.date(2009, 5, 27)
        qs = Scrobble.objects.day(d).order_by("date")

        # check scrobble count
        self.assertEqual(qs.count(), 25)

        # check start and end dates of date range
        first = qs.first().date
        last = qs.last().date
        self.assertGreaterEqual(
            first, datetime.datetime(2009, 5, 27, tzinfo=datetime.timezone.utc)
        )
        self.assertLess(
            last, datetime.datetime(2010, 5, 27, tzinfo=datetime.timezone.utc)
        )

    @freeze_time("2009-05-17")
    def test_today(self):
        """Tests scrobble_server.core.querysets.TimeFilter.today"""
        qs1 = Scrobble.objects.today()
        qs2 = Scrobble.objects.filter(date__date=datetime.date(2009, 5, 17))
        self.assertEqual(list(qs1), list(qs2))


class CounterTests(TestCase):
    """
    Tests for scrobble_server.core.querysets.Counters

    The resulting lists with scrobble counts are tested against the known
    counts of the scrobble data in the fixture. The expected values can be
    found in tests/data.py
    """

    fixtures = ["user_and_profile", "charts_testdata"]

    def test_counts_yearly(self):
        """Tests scrobble_server.core.querysets.Counters.counts_yearly"""
        counts = Scrobble.objects.counts_yearly()
        exp = data.counts_yearly
        self.assertEqual(list(counts), exp)

    def test_counts_monthly(self):
        """Tests scrobble_server.core.querysets.Counters.counts_monthly"""
        counts = Scrobble.objects.year(datetime.date(2009, 1, 1)).counts_monthly()
        exp = data.counts_monthly_2009
        self.assertEqual(list(counts), exp)

    def test_counts_weekly(self):
        """Tests scrobble_server.core.querysets.Counters.counts_weekly"""
        counts = Scrobble.objects.month(datetime.date(2009, 5, 1)).counts_weekly()
        exp = data.counts_weekly_2009_05
        self.assertEqual(list(counts), exp)

    def test_counts_daily(self):
        """Tests scrobble_server.core.querysets.Counters.counts_daily"""
        counts = Scrobble.objects.week(datetime.date(2009, 5, 11)).counts_daily()
        exp = data.counts_daily_2009_05_11_to_2009_05_17
        self.assertEqual(list(counts), exp)


class TopAggregationTests(TestCase):
    """
    Tests for scrobble_server.core.querysets.TopAggregation

    The toplist aggregation methods (top_artists, top_albums, top_tracks) are
    tested by loading a fixture with scrobble data and known counts. The
    calculated toplists are compared to the known lists saved in
    tests/data.py
    Five different time intervals are tested for each method:
    * overall: All scrobble data (which is 2007 to 2009 inclusive)
    * 2009
    * May 2009
    * week 20 of 2009 (May 11th to May 17th inclusive)
    * May 11th 2009

    Right now top_listeners is not being tested because the fixture only
    contains listens from a single user.
    """

    fixtures = ["user_and_profile", "charts_testdata"]

    def test_top_artists(self):
        """Tests scrobble_server.core.querysets.TopAggregation.top_artists"""
        # overall
        toplist = Scrobble.objects.top_artists()
        exp = data.top_artists_overall
        self.assertEqual(list(toplist), exp)

        # 2009
        toplist = Scrobble.objects.year(datetime.date(2009, 1, 1)).top_artists()
        exp = data.top_artists_2009
        self.assertEqual(list(toplist), exp)

        # May 2009
        toplist = Scrobble.objects.month(datetime.date(2009, 5, 1)).top_artists()
        exp = data.top_artists
        self.assertEqual(list(toplist), exp)

        # 2009 week 20
        toplist = Scrobble.objects.week(datetime.date(2009, 5, 11)).top_artists()
        exp = data.top_artists_2009_week_20
        self.assertEqual(list(toplist), exp)

        # May 11th 2009
        toplist = Scrobble.objects.day(datetime.date(2009, 5, 11)).top_artists()
        exp = data.top_artists_2009_05_11
        self.assertEqual(list(toplist), exp)

    def test_top_albums(self):
        """Tests scrobble_server.core.querysets.TopAggregation.top_albums"""
        # overall
        toplist = Scrobble.objects.top_albums()
        exp = data.top_albums_overall
        self.assertEqual(list(toplist), exp)

        # 2009
        toplist = Scrobble.objects.year(datetime.date(2009, 1, 1)).top_albums()
        exp = data.top_albums_2009
        self.assertEqual(list(toplist), exp)

        # May 2009
        toplist = Scrobble.objects.month(datetime.date(2009, 5, 1)).top_albums()
        exp = data.top_albums
        self.assertEqual(list(toplist), exp)

        # 2009 week 20
        toplist = Scrobble.objects.week(datetime.date(2009, 5, 11)).top_albums()
        exp = data.top_albums_2009_week_20
        self.assertEqual(list(toplist), exp)

        # May 11th 2009
        toplist = Scrobble.objects.day(datetime.date(2009, 5, 11)).top_albums()
        exp = data.top_albums_2009_05_11
        self.assertEqual(list(toplist), exp)

    def test_top_tracks(self):
        """Tests scrobble_server.core.querysets.TopAggregation.top_tracks"""
        # overall
        toplist = Scrobble.objects.top_tracks()
        exp = data.top_tracks_overall
        self.assertEqual(list(toplist), exp)

        # 2009
        toplist = Scrobble.objects.year(datetime.date(2009, 1, 1)).top_tracks()
        exp = data.top_tracks_2009
        self.assertEqual(list(toplist), exp)

        # May 2009
        toplist = Scrobble.objects.month(datetime.date(2009, 5, 1)).top_tracks()
        exp = data.top_tracks
        self.assertEqual(list(toplist), exp)

        # 2009 week 20
        toplist = Scrobble.objects.week(datetime.date(2009, 5, 11)).top_tracks()
        exp = data.top_tracks_2009_week_20
        self.assertEqual(list(toplist), exp)

        # May 11th 2009
        toplist = Scrobble.objects.day(datetime.date(2009, 5, 11)).top_tracks()
        exp = data.top_tracks_2009_05_11
        self.assertEqual(list(toplist), exp)
