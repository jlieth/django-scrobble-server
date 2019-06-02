from django.conf.urls import include, url

# Audioscrobbler Protocol 1.2
urlpatterns = [
    url(r"^api/1.2/", include("scrobble_server.api.v12.urls", namespace="api_v1.2"))
]
