from django.conf.urls import url
from scrobble_server.api.v12.views.handshake import handshake
from scrobble_server.api.v12.views.nowplaying import nowplaying
from scrobble_server.api.v12.views.scrobble import scrobble


app_name = "api_v1.2"

urlpatterns = [
    url("handshake$", handshake, name="handshake"),
    url("nowplaying$", nowplaying, name="nowplaying"),
    url("scrobble$", scrobble, name="scrobble"),
]
