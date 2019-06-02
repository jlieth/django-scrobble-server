from django.test import TestCase
from django.urls import reverse

from .base_submissions import BaseSubmission


class NowPlayingTests(BaseSubmission, TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = reverse("api_v1.2:nowplaying")
        cls.required_params = ["s", "a", "t", "b", "l", "n"]
        super().setUpClass()

    @property
    def request_dict(self):
        return {
            "s": self.session_id,
            "a": self.artist_name,
            "t": self.track_title,
            "b": self.album_title,
            "l": self.length,
            "n": self.tracknumber,
        }
