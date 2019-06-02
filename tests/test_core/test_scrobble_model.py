import calendar
import sys

from django.test import TestCase
from django.utils import timezone

from scrobble_server.core.models.submissions import Scrobble
from .test_base_submission_model import BaseSubmissionTests


class ScrobbleTests(BaseSubmissionTests, TestCase):
    model = Scrobble

    def test_date(self):
        now = timezone.now()
        if sys.version_info.major == 2:
            timestamp = calendar.timegm(now.timetuple())
        else:
            timestamp = now.timestamp()

        scrobble = Scrobble.objects.create(
            profile=self.profile,
            artist_name="foo",
            track_title="bar",
            timestamp=timestamp,
        )

        self.assertEqual(scrobble.date.utctimetuple(), now.utctimetuple())
