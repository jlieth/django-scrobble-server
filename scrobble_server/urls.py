from django.conf import settings
from django.urls import include, path


urlpatterns = []

if "scrobble_server.api.v12" in settings.INSTALLED_APPS:
    urlpatterns += [path("api/v1.2/", include("scrobble_server.api.v12.urls"))]
