import time

from django.test import TestCase
from django.urls import reverse

from .base_submissions import BaseSubmission


class ScrobbleTests(BaseSubmission, TestCase):
    def setUp(self):
        self.timestamp = int(time.time())
        self.source = "P"
        self.rating = ""

        self.url = reverse("api_v1.2:scrobble")
        self.required_params = ["s"]
        super().setUp()

    def test_negative_timestamp(self):
        # negative timestamp should yield status_code=400 and FAILED [...]
        self.timestamp = -1
        self.expect_400_FAILED(self.request_dict)

    def test_request_creates_scrobble_object(self):
        scrobble = self.profile.scrobbles.filter(timestamp=self.timestamp)
        self.assertFalse(scrobble.exists())

        self.expect_200_OK(self.request_dict)
        scrobble = self.profile.scrobbles.filter(timestamp=self.timestamp)
        self.assertTrue(scrobble.exists())

    def test_scrobble_count_increase(self):
        scrobble_count_before = self.profile.scrobbles.count()
        self.expect_200_OK(self.request_dict)
        scrobble_count_after = self.profile.scrobbles.count()
        self.assertEqual(scrobble_count_after, scrobble_count_before + 1)

    def test_sending_same_scrobble_twice(self):
        self.timestamp = int(time.time()) + 1
        self.expect_200_OK(self.request_dict)
        self.expect_200_OK(self.request_dict)

    def test_same_scrobble_doesnt_change_scrobble_count(self):
        self.expect_200_OK(self.request_dict)
        scrobble_count1 = self.profile.scrobbles.count()
        self.expect_200_OK(self.request_dict)
        scrobble_count2 = self.profile.scrobbles.count()
        self.assertEqual(scrobble_count1, scrobble_count2)

    @property
    def request_dict(self):
        return {
            "s": self.session_id,
            "a[0]": self.artist_name,
            "t[0]": self.track_title,
            "i[0]": self.timestamp,
            "o[0]": self.source,
            "r[0]": self.rating,
            "b[0]": self.album_title,
            "l[0]": self.length,
            "n[0]": self.tracknumber,
        }
