from django.test import TestCase
from django.utils import timezone

from scrobble_server.core.models.submissions import Scrobble
from .test_base_submission_model import BaseSubmissionTests


class ScrobbleTests(BaseSubmissionTests, TestCase):
    model = Scrobble

    def test_date(self):
        now = timezone.now()
        timestamp = now.timestamp()

        scrobble = Scrobble.objects.create(
            profile=self.profile,
            artist_name="foo",
            track_title="bar",
            timestamp=timestamp,
        )

        self.assertEqual(scrobble.date.utctimetuple(), now.utctimetuple())
