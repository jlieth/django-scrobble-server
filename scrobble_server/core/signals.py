import datetime

from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from scrobble_server.core.models.profile import Profile
from scrobble_server.core.models.music import Album, AlbumTrackUnit, Artist, Track
from scrobble_server.core.models.submissions import NowPlaying, Scrobble

User = get_user_model()


@receiver(post_save, sender=User)
def get_or_create_profile_on_user_save(sender, instance, **kwargs):
    Profile.objects.get_or_create(user=instance)


@receiver(post_delete, sender=Profile)
def create_new_profile_if_user_still_exists(sender, instance, **kwargs):
    user = instance.user
    # user still in db?
    user_exists = User.objects.filter(pk=user.pk).exists()
    # if so, create new p and attach it to the user
    if user_exists:
        Profile.objects.create(user=user)


@receiver(pre_save, sender=NowPlaying)
def process_nowplaying(sender, instance, **kwargs):
    # delete stale nowplayings of this user
    profile = instance.profile
    NowPlaying.objects.filter(profile=profile).delete()


@receiver(pre_save, sender=Scrobble)
def process_scrobble(sender, instance, **kwargs):
    # set utc date
    timestamp = instance.timestamp
    dt = datetime.datetime.utcfromtimestamp(timestamp)
    instance.date = timezone.make_aware(dt, timezone.utc)


@receiver(pre_save, sender=NowPlaying)
@receiver(pre_save, sender=Scrobble)
def process_any_submission(sender, instance, **kwargs):
    # make sure length and tracknumber are not None
    instance.length = instance.length or 0
    instance.tracknumber = instance.tracknumber or 0


@receiver(pre_save, sender=NowPlaying)
@receiver(pre_save, sender=Scrobble)
def link_submission_object_to_music_objects(sender, instance, **kwargs):
    # get_or_create and link music objects
    if not instance.artist:
        artist_name = instance.artist_name
        artist, created = Artist.objects.get_or_create(
            name__iexact=artist_name, defaults={"name": artist_name}
        )
        instance.artist = artist

    if not instance.track:
        track_title = instance.track_title
        track, created = Track.objects.get_or_create(
            title__iexact=track_title, artist=artist, defaults={"title": track_title}
        )
        instance.track = track

    if not instance.album and instance.album_title:
        album_title = instance.album_title
        album, created = Album.objects.get_or_create(
            title__iexact=album_title, artist=artist, defaults={"title": album_title}
        )
        instance.album = album
        AlbumTrackUnit.objects.get_or_create(
            track=track,
            album=album,
            tracknumber=instance.tracknumber,
            defaults={"length": instance.length},
        )
