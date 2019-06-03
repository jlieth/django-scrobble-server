from scrobble_server.core.models.music import Artist, Album, AlbumTrackUnit, Track
from scrobble_server.core.models.profile import Profile
from scrobble_server.core.models.submissions import Scrobble


class BaseSubmissionTests:
    fixtures = ["user_and_profile"]
    model = None

    def setUp(self):
        self.profile = Profile.objects.first()
        self.artist_name = "foo"
        self.track_title = "bar"
        self.album_title = "baz"
        self.timestamp = 1234567890
        self.length = None
        self.tracknumber = None

    def create_object(self):
        kwargs = {
            "profile": self.profile,
            "artist_name": self.artist_name,
            "track_title": self.track_title,
            "album_title": self.album_title,
            "length": self.length,
            "tracknumber": self.tracknumber,
        }
        if self.model == Scrobble:
            kwargs["timestamp"] = self.timestamp
        return self.model.objects.create(**kwargs)

    def test_str(self):
        obj = self.create_object()
        s = "[%s] %s - %s" % (obj.date, self.artist_name, self.track_title)
        self.assertEqual(str(obj), s)

    def test_length_and_tracknumber_are_numeric(self):
        self.length = None
        self.tracknumber = None
        obj = self.create_object()
        self.assertEqual(obj.length, 0)
        self.assertEqual(obj.tracknumber, 0)

    def test_autocreating_music_objects_on_submission(self):
        # music objects don't exist yet
        self.assertRaises(
            Artist.DoesNotExist, Artist.objects.get, name=self.artist_name
        )
        self.assertRaises(
            Track.DoesNotExist,
            Track.objects.get,
            artist__name=self.artist_name,
            title=self.track_title,
        )
        self.assertRaises(
            Album.DoesNotExist,
            Album.objects.get,
            artist__name=self.artist_name,
            title=self.album_title,
        )

        obj = self.create_object()

        # music objects where created
        artist_exists = Artist.objects.filter(name=self.artist_name).exists()
        self.assertTrue(artist_exists)

        track_exists = Track.objects.filter(
            artist__name=self.artist_name, title=self.track_title
        ).exists()
        self.assertTrue(track_exists)

        album_exists = Album.objects.filter(
            artist__name=self.artist_name, title=self.album_title
        ).exists()
        self.assertTrue(album_exists)

        unit_exists = AlbumTrackUnit.objects.filter(
            track__title=self.track_title, album__title=self.album_title
        ).exists()
        self.assertTrue(unit_exists)

        # make sure they were linked to the nowplaying object
        artist = Artist.objects.get(name=self.artist_name)
        track = Track.objects.get(artist__name=self.artist_name, title=self.track_title)
        album = Album.objects.get(artist__name=self.artist_name, title=self.album_title)

        self.assertEqual(obj.artist, artist)
        self.assertEqual(obj.track, track)
        self.assertEqual(obj.album, album)

    def test_getting_existing_music_objects_on_submission(self):
        """
        Test that existing music objects are used when a submission object
        (NowPlaying or Scrobble) is created.
        """
        artist = Artist.objects.create(name=self.artist_name)
        track = Track.objects.create(title=self.track_title, artist=artist)
        album = Album.objects.create(title=self.album_title, artist=artist)

        obj = self.create_object()

        # make sure the object got linked to the existing music objects
        self.assertEqual(obj.artist, artist)
        self.assertEqual(obj.track, track)
        self.assertEqual(obj.album, album)

    def test_saving_submission_obj(self):
        """
        Creating the submission object establishes links to music objects.
        Saving the submission object any subsequent times shouldn't change
        the links.
        """
        obj = self.create_object()

        artist_before = obj.artist
        track_before = obj.track
        album_before = obj.album

        obj.save()

        self.assertEqual(obj.artist, artist_before)
        self.assertEqual(obj.track, track_before)
        self.assertEqual(obj.album, album_before)
