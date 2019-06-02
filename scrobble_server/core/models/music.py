from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")

    class Meta:
        ordering = ["artist", "title"]
        unique_together = ["title", "artist"]

    def __str__(self):
        return "%s" % self.title


class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="tracks")

    class Meta:
        ordering = ["artist", "title"]
        unique_together = ["title", "artist"]

    def __str__(self):
        return "%s" % self.title


class AlbumTrackUnit(models.Model):
    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.CASCADE)
    track = models.ForeignKey(Track, related_name="albums", on_delete=models.CASCADE)
    tracknumber = models.PositiveIntegerField(null=True, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ["album", "tracknumber"]
        unique_together = ["album", "track", "tracknumber"]

    def __str__(self):
        return "%s on %s" % (self.track.title, self.album.title)
