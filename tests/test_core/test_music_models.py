from django.db.utils import IntegrityError
from django.test import TestCase

from scrobble_server.core.models.music import Artist, Album, AlbumTrackUnit, Track


class MusicTests(TestCase):
    def setUp(self):
        self.artist_name = "foo"
        self.track_title = "bar"
        self.album_title = "baz"

    def test_strs(self):
        artist = Artist(name=self.artist_name)
        self.assertEqual(str(artist), self.artist_name)

        album = Album(title=self.album_title, artist=artist)
        self.assertEqual(str(album), self.album_title)

        track = Track(title=self.track_title, artist=artist)
        self.assertEqual(str(track), self.track_title)

        unit = AlbumTrackUnit(track=track, album=album)
        self.assertEqual(str(unit), "%s on %s" % (track.title, album.title))

    def test_artist_uniqueness(self):
        """Artist objects should be unique for name"""
        Artist.objects.create(name=self.artist_name)
        self.assertRaisesMessage(
            IntegrityError,
            "UNIQUE constraint failed: core_artist.name",
            Artist.objects.create,
            name=self.artist_name,
        )

    def test_album_uniqueness(self):
        """Album objects should be unique for (title, artist)"""
        artist = Artist.objects.create(name=self.artist_name)
        Album.objects.create(title=self.album_title, artist=artist)
        self.assertRaisesMessage(
            IntegrityError,
            "UNIQUE constraint failed: core_album.title, core_album.artist_id",
            Album.objects.create,
            title=self.album_title,
            artist=artist,
        )

    def test_track_uniqueness(self):
        """Track objects should be unique for (title, artist)"""
        artist = Artist.objects.create(name=self.artist_name)
        Track.objects.create(title=self.album_title, artist=artist)
        self.assertRaisesMessage(
            IntegrityError,
            "UNIQUE constraint failed: core_track.title, core_track.artist_id",
            Track.objects.create,
            title=self.album_title,
            artist=artist,
        )

    def test_album_track_unit_uniqueness(self):
        """AlbumTrackUnit objects should be unique for (album, track, tracknumber)"""
        artist = Artist.objects.create(name=self.artist_name)
        album = Album.objects.create(title=self.album_title, artist=artist)
        track = Track.objects.create(title=self.album_title, artist=artist)
        AlbumTrackUnit.objects.create(track=track, album=album, tracknumber=1)
        self.assertRaisesMessage(
            IntegrityError,
            (
                "UNIQUE constraint failed: core_albumtrackunit.album_id, "
                "core_albumtrackunit.track_id, core_albumtrackunit.tracknumber"
            ),
            AlbumTrackUnit.objects.create,
            track=track,
            album=album,
            tracknumber=1,
        )
