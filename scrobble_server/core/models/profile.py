from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from scrobble_server.core.models.cache import ChartsCache

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to="avatars", blank=True, null=True)

    charts = GenericRelation(ChartsCache, related_query_name="content_object")

    def __str__(self):
        return "%s's profile" % self.user

    def get_recent(self, page=1):
        scrobbles = self.scrobbles.order_by("-date").values(
            "date", "artist__name", "track__title"
        )
        p = Paginator(scrobbles, 10)
        return p.page(page).object_list

    def get_nowplaying(self):
        if not self.nowplaying.exists():
            return None

        nowplaying = self.nowplaying.first()
        if nowplaying.is_over():
            self.nowplaying.all().delete()
            return None

        return nowplaying

    def last_scrobble_is_nowplaying(self):
        nowplaying = self.get_nowplaying()
        if not nowplaying:
            return False

        scrobble = self.scrobbles.order_by("-timestamp").first()
        if not scrobble:
            return False

        same_track = scrobble.track == nowplaying.track
        if not same_track:
            return False

        scrobbled_after_nowplaying_began = scrobble.date > nowplaying.date
        if not scrobbled_after_nowplaying_began:
            return False

        return True
