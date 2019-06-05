from django.urls import path

from scrobble_server.api.v12.views.handshake import handshake
from scrobble_server.api.v12.views.nowplaying import nowplaying
from scrobble_server.api.v12.views.scrobble import scrobble


app_name = "api_v1.2"

urlpatterns = [
    path("handshake", handshake, name="handshake"),
    path("nowplaying", nowplaying, name="nowplaying"),
    path("scrobble", scrobble, name="scrobble"),
]
