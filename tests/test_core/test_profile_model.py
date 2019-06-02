import calendar
import sys

from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.test import TestCase

from scrobble_server.core.models.profile import Profile
from scrobble_server.core.models.submissions import NowPlaying, Scrobble

User = get_user_model()


class ProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test", password="password")

    def test_profile_str(self):
        self.assertEqual(str(self.user.profile), "%s's profile" % self.user)

    def test_profile_multiplicity(self):
        """
        Every user must have exactly one p at any time.
        """
        # pofile was autocreated for the user
        self.assertIsInstance(self.user.profile, Profile)

        # new p is created when the previous one is deleted
        self.user.profile.delete()
        self.assertIsInstance(self.user.profile, Profile)

        # can't create second p for same user
        with self.assertRaises(IntegrityError):
            Profile.objects.create(user=self.user)

    def test_get_nowplaying(self):
        # should be None while no nowplaying exists
        self.assertIsNone(self.user.profile.get_nowplaying())

        # should be None if saved nowplaying is over
        np1 = NowPlaying.objects.create(
            profile=self.user.profile, artist_name="foo", track_title="bar", length=0
        )

        self.assertTrue(np1.is_over())
        self.assertIsNone(self.user.profile.get_nowplaying())

        # stale nowplaying should have been deleted now
        with self.assertRaises(NowPlaying.DoesNotExist):
            np1.refresh_from_db()

        # still playing: should be the nowplaying object
        np2 = NowPlaying.objects.create(
            profile=self.user.profile, artist_name="foo", track_title="bar", length=100
        )

        self.assertFalse(np2.is_over())
        self.assertEqual(self.user.profile.get_nowplaying(), np2)

    def test_last_scrobble_is_nowplaying(self):
        # should be False if no nowplaying exists
        self.assertIsNone(self.user.profile.get_nowplaying())
        self.assertFalse(self.user.profile.last_scrobble_is_nowplaying())

        # create nowplaying
        np = NowPlaying.objects.create(
            profile=self.user.profile, artist_name="foo", track_title="bar", length=100
        )

        # should be False if nothing has been scrobbled
        scrobble = Scrobble.objects.filter(profile=self.user.profile)
        self.assertFalse(scrobble.exists())
        self.assertFalse(self.user.profile.last_scrobble_is_nowplaying())

        # create scrobble with different track
        scrobble = Scrobble.objects.create(
            profile=self.user.profile,
            artist_name="foo",
            track_title="i'm different",
            timestamp=0,
        )

        # should be False because different track
        self.assertNotEqual(np.track, scrobble.track)
        self.assertFalse(self.user.profile.last_scrobble_is_nowplaying())

        # create scrobble with same track but way back in the past
        scrobble = Scrobble.objects.create(
            profile=self.user.profile, artist_name="foo", track_title="bar", timestamp=1
        )

        # should be False because track was scrobbled before nowplaying started
        self.assertLess(scrobble.date, np.date)
        self.assertFalse(self.user.profile.last_scrobble_is_nowplaying())

        # create scrobble with timestamp after nowplaying started
        if sys.version_info.major == 2:
            timestamp = calendar.timegm(np.date.timetuple())
        else:
            timestamp = np.date.timestamp()

        scrobble = Scrobble.objects.create(
            profile=self.user.profile,
            artist_name="foo",
            track_title="bar",
            timestamp=timestamp + 1,
        )

        # should be True now
        self.assertGreater(scrobble.date, np.date)
        self.assertTrue(self.user.profile.last_scrobble_is_nowplaying())
