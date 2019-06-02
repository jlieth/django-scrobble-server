from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from scrobble_server.core.models.submissions import NowPlaying
from scrobble_server.api.v12.decorators import required_params
from scrobble_server.api.v12.models import ScrobbleSession


@csrf_exempt
@require_POST
@required_params(["s", "a", "t", "b", "l", "n"])
def nowplaying(request):
    params = request.POST.dict()

    # check session
    session_key = params["s"]
    try:
        profile = ScrobbleSession.objects.get(key=session_key).profile
    except ScrobbleSession.DoesNotExist:
        return HttpResponseBadRequest("BADSESSION")

    data = {
        "profile": profile.pk,
        "artist_name": params["a"],
        "track_title": params["t"],
        "album_title": params["b"],
        "length": params["l"],
        "tracknumber": params["n"],
    }

    # create form
    excluded_fields = ["artist", "album", "track", "date"]
    NowPlayingForm = modelform_factory(NowPlaying, exclude=excluded_fields)
    form = NowPlayingForm(data)

    # see if the form validates
    if not form.is_valid():
        return HttpResponseBadRequest("FAILED request invalid")
    else:
        form.save()
        return HttpResponse("OK")
