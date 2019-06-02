from collections import namedtuple
import datetime

from freezegun import freeze_time

from django.test import TestCase

from scrobble_server.core.charts import TopList
from scrobble_server.core.models.profile import Profile
from scrobble_server.core.models.submissions import Scrobble

from tests import data

TopListTestCase = namedtuple("TopListTestCase", "timespan date expected")


class TopListTests(TestCase):
    fixtures = ["user_and_profile", "charts_testdata"]

    def setUp(self):
        self.profile = Profile.objects.first()

    def test_combine_results(self):
        """Tests scrobble_server.core.charts.TopList.combine_results"""
        combined = TopList.combine_results(
            data.toplistdata_artists_2007, data.toplistdata_artists_2008
        )
        self.assertEqual(combined, data.toplistdata_artists_2007_and_2008)

    @freeze_time("2009-05-17")
    def test_today_in_range(self):
        """
        Tests scrobble_server.core.charts.TopList.today_in_range

        This tests basically creates TopList instances with different arguments
        and checks whether the (faked) date of today 2009-05-17 is in the
        indicated range of time. For every timespan one case is tested where
        the result should be True and one where it should be False (except for
        timespan=all, which should always include today). Cases tested:
        * should be in range for timespan=all and fixpoint=1970-01-01
        * should not be in range for timespan=year and fixpoint=2008-01-01
        * should be in range for timespan=year and fixpoint=2009-01-01
        * should not be in range for timespan=month and fixpoint=2009-04-01
        * should be in range for timespan=month and fixpoint=2009-05-01
        * should not be in range for timespan=week and fixpoint=2009-05-20
        * should be in range for timespan=week and fixpoint=2009-05-11
        * should not be in range for timespan=day and fixpoint=2009-05-20
        * should be in range for timespan=day and fixpoint=2009-05-17
        """
        test_cases = [
            TopListTestCase(
                timespan="all", date=datetime.date(1970, 1, 1), expected=True
            ),
            TopListTestCase(
                timespan="year", date=datetime.date(2008, 1, 1), expected=False
            ),
            TopListTestCase(
                timespan="year", date=datetime.date(2009, 1, 1), expected=True
            ),
            TopListTestCase(
                timespan="month", date=datetime.date(2009, 4, 1), expected=False
            ),
            TopListTestCase(
                timespan="month", date=datetime.date(2009, 5, 1), expected=True
            ),
            TopListTestCase(
                timespan="week", date=datetime.date(2009, 5, 20), expected=False
            ),
            TopListTestCase(
                timespan="week", date=datetime.date(2009, 5, 11), expected=True
            ),
            TopListTestCase(
                timespan="day", date=datetime.date(2009, 5, 20), expected=False
            ),
            TopListTestCase(
                timespan="day", date=datetime.date(2009, 5, 17), expected=True
            ),
        ]

        for case in test_cases:
            tl = TopList(self.profile, "artists", case.timespan, case.date)
            self.assertEqual(tl.today_in_range, case.expected)

    def test_qs(self):
        """
        Tests scrobble_server.core.charts.TopList.qs

        This test compares the returned queryset from TopList.qs against the
        expected queryset for the given date and timespan.
        """
        d = datetime.date(2009, 5, 17)
        week_start = datetime.date(2009, 5, 11)

        test_cases = [
            TopListTestCase(timespan="all", date=d, expected=Scrobble.objects.all()),
            TopListTestCase(
                timespan="year",
                date=d,
                expected=Scrobble.objects.filter(date__year=2009),
            ),
            TopListTestCase(
                timespan="month",
                date=d,
                expected=Scrobble.objects.filter(date__year=2009, date__month=5),
            ),
            TopListTestCase(
                timespan="week",
                date=d,
                expected=Scrobble.objects.filter(date__date__range=[week_start, d]),
            ),
            TopListTestCase(
                timespan="day", date=d, expected=Scrobble.objects.filter(date__date=d)
            ),
        ]

        for case in test_cases:
            tl = TopList(self.profile, "artists", case.timespan, case.date)
            self.assertEqual(list(tl.qs), list(case.expected))
