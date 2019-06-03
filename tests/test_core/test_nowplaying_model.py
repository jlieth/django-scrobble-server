from django.test import TestCase

from scrobble_server.core.models.submissions import NowPlaying
from .test_base_submission_model import BaseSubmissionTests


class NowPlayingTests(BaseSubmissionTests, TestCase):
    model = NowPlaying

    def test_nowplaying_multiplicity(self):
        """
        There can be at most one NowPlaying object per p at once.
        NowPlaying has a pre_save signal receiver connected that should
        delete all NowPlaying objects connected to the same p as
        the object about to be saved.
        """
        # count==0 in the beginning
        self.assertEqual(self.profile.nowplaying.count(), 0)

        # count==1 after creating one
        np1 = self.profile.nowplaying.create(artist_name="a", track_title="b")
        self.assertEqual(self.profile.nowplaying.count(), 1)

        # count==1 after creating another one
        self.profile.nowplaying.create(artist_name="c", track_title="d")
        self.assertEqual(self.profile.nowplaying.count(), 1)

        # np1 must have been deleted from db by creation of the new nowplaying
        with self.assertRaises(NowPlaying.DoesNotExist):
            NowPlaying.objects.get(pk=np1.pk)

        # for good measure, test again with model save method
        np2 = NowPlaying(profile=self.profile, artist_name="e", track_title="f")
        np2.save()
        self.assertEqual(self.profile.nowplaying.count(), 1)

    def test_is_not_over(self):
        self.length = 1000
        obj = self.create_object()
        self.assertFalse(obj.is_over())

        self.length = 0
        obj = self.create_object()
        self.assertTrue(obj.is_over())
