from django.db import models
from django.utils import timezone

from scrobble_server.core.models.music import Artist, Album, Track, AlbumTrackUnit
from scrobble_server.core.querysets import ScrobbleQuerySet


class BaseSubmission(models.Model):
    date = models.DateTimeField(default=timezone.now, editable=False)
    artist_name = models.CharField(max_length=255)
    track_title = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255, blank=True)
    length = models.PositiveIntegerField(blank=True, null=True)
    tracknumber = models.PositiveIntegerField(blank=True, null=True)

    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    artist = models.ForeignKey("Artist", on_delete=models.PROTECT)
    track = models.ForeignKey("Track", on_delete=models.PROTECT)
    album = models.ForeignKey("Album", on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "[%s] %s - %s" % (self.date, self.artist_name, self.track_title)

    def save(self, *args, **kwargs):
        if not self.pk:  # on_create
            self._link_to_music_objects()

        super().save(*args, **kwargs)

    def _link_to_music_objects(self):
        # artist
        artist_name = self.artist_name
        artist, created = Artist.objects.get_or_create(
            name__iexact=artist_name, defaults={"name": artist_name}
        )
        self.artist = artist

        # track
        track_title = self.track_title
        track, created = Track.objects.get_or_create(
            title__iexact=track_title, artist=artist, defaults={"title": track_title}
        )
        self.track = track

        # album
        if self.album_title:
            album_title = self.album_title
            album, created = Album.objects.get_or_create(
                title__iexact=album_title,
                artist=artist,
                defaults={"title": album_title},
            )
            self.album = album
            AlbumTrackUnit.objects.get_or_create(
                track=track,
                album=album,
                tracknumber=self.tracknumber,
                defaults={"length": self.length},
            )


class NowPlaying(BaseSubmission):
    class Meta:
        default_related_name = "nowplaying"
        ordering = ["-date"]
        verbose_name = "Now playing track"
        verbose_name_plural = "Now playing tracks"

    def is_over(self):
        playback_end = self.date + timezone.timedelta(seconds=self.length)
        now = timezone.now()
        return now > playback_end


class Scrobble(BaseSubmission):
    timestamp = models.PositiveIntegerField()

    objects = ScrobbleQuerySet.as_manager()

    class Meta:
        base_manager_name = "objects"
        default_related_name = "scrobbles"
        indexes = [models.Index(fields=["date"])]
        ordering = ["-date"]
        unique_together = ["profile", "timestamp"]
