import uuid

from django.db import models
from django.utils import timezone


class Client(models.Model):
    client_id = models.CharField(max_length=255)
    client_version = models.CharField(max_length=255)
    banned = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = "v12"
        unique_together = ["client_id", "client_version"]

    def __str__(self):
        return "%s@%s" % (self.client_id, self.client_version)


def make_session_key():
    while True:
        key = uuid.uuid4().hex
        if not ScrobbleSession.objects.filter(key=key).exists():
            return key


class ScrobbleSession(models.Model):
    key = models.CharField(max_length=32, default=make_session_key)
    created = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey("core.Profile", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        default_related_name = "scrobble_sessions"
        indexes = [models.Index(fields=["key"])]
        ordering = ["-created"]

    def __str__(self):
        return "{} scrobbling with {} on {}".format(
            self.profile.user.username, self.client, self.created
        )


class MD5AuthHash(models.Model):
    hash = models.CharField(max_length=32)
    profile = models.OneToOneField(
        "core.Profile", on_delete=models.CASCADE, null=True, related_name="md5hash"
    )
