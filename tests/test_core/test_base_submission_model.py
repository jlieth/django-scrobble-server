from django.contrib.auth import get_user_model

from scrobble_server.core.models.music import Artist, Album, AlbumTrackUnit, Track
from scrobble_server.core.models.submissions import Scrobble

User = get_user_model()


class BaseSubmissionTests:
    model = None

    def setUp(self):
        user = User.objects.create(username="test", password="password")
        self.profile = user.profile
        self.artist_name = "foo"
        self.track_title = "bar"
        self.album_title = "baz"
        self.timestamp = 1234567890
        self.length = None
        self.tracknumber = None
        self.obj = None

    def tearDown(self):
        self.delete_objects()

    def delete_objects(self):
        if self.obj:
            if isinstance(self.obj.track, Track) and isinstance(self.obj.album, Album):
                AlbumTrackUnit.objects.filter(
                    track=self.obj.track, album=self.obj.album
                ).delete()

            for music_object in [self.obj.track, self.obj.album, self.obj.artist]:
                if hasattr(music_object, "delete"):
                    music_object.delete()

            self.obj.delete()

    def create_submission_object(self):
        self.delete_objects()
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
        self.obj = self.model.objects.create(**kwargs)

    def test_str(self):
        self.create_submission_object()
        s = "[%s] %s - %s" % (self.obj.date, self.artist_name, self.track_title)
        self.assertEqual(str(self.obj), s)

    def test_length_and_tracknumber_are_numeric(self):
        self.length = None
        self.tracknumber = None
        self.create_submission_object()
        self.assertEqual(self.obj.length, 0)
        self.assertEqual(self.obj.tracknumber, 0)

    def test_autocreating_music_objects_on_submission(self):
        # music objects don't exist yet
        with self.assertRaises(Artist.DoesNotExist):
            Artist.objects.get(name=self.artist_name)
        with self.assertRaises(Track.DoesNotExist):
            Track.objects.get(artist__name=self.artist_name, title=self.track_title)
        with self.assertRaises(Album.DoesNotExist):
            Album.objects.get(artist__name=self.artist_name, title=self.album_title)
        with self.assertRaises(AlbumTrackUnit.DoesNotExist):
            AlbumTrackUnit.objects.get(
                track__title=self.track_title, album__title=self.album_title
            )

        self.create_submission_object()

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

        self.assertEqual(self.obj.artist, artist)
        self.assertEqual(self.obj.track, track)
        self.assertEqual(self.obj.album, album)

    def test_getting_existing_music_objects_on_submission(self):
        """
        Test that existing music objects are used when a submission object
        (NowPlaying or Scrobble) is created.
        """
        artist = Artist.objects.create(name=self.artist_name)
        track = Track.objects.create(title=self.track_title, artist=artist)
        album = Album.objects.create(title=self.album_title, artist=artist)

        self.create_submission_object()

        # make sure the object got linked to the existing music objects
        self.assertEqual(self.obj.artist, artist)
        self.assertEqual(self.obj.track, track)
        self.assertEqual(self.obj.album, album)

    def test_saving_submission_obj(self):
        """
        Creating the submission object establishes links to music objects.
        Saving the submission object any subsequent times shouldn't change
        the links.
        """
        self.create_submission_object()

        artist_before = self.obj.artist
        track_before = self.obj.track
        album_before = self.obj.album

        self.obj.save()

        self.assertEqual(self.obj.artist, artist_before)
        self.assertEqual(self.obj.track, track_before)
        self.assertEqual(self.obj.album, album_before)
