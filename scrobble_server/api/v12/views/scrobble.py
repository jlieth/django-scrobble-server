from itertools import zip_longest
from pyquerystring import parse

from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from scrobble_server.core.models.submissions import Scrobble
from scrobble_server.api.v12.decorators import required_params
from scrobble_server.api.v12.models import ScrobbleSession


@csrf_exempt
@require_POST
@required_params(["s"])
def scrobble(request):
    # check session
    session_key = request.POST.get("s")
    try:
        profile = ScrobbleSession.objects.get(key=session_key).profile
    except ScrobbleSession.DoesNotExist:
        return HttpResponseBadRequest("BADSESSION")

    # turn query into usable format
    query_string = request.POST.urlencode()
    data = parse(query_string)

    timestamps = data.get("i", [])
    artists = data.get("a", [])
    tracks = data.get("t", [])
    albums = data.get("b", [])
    lengths = data.get("l", [])
    tracknumbers = data.get("n", [])

    # create scrobble form
    excluded_fields = ["artist", "album", "track", "date"]
    ScrobbleForm = modelform_factory(Scrobble, exclude=excluded_fields)

    for i, a, t, b, l, n in zip_longest(
        timestamps, artists, tracks, albums, lengths, tracknumbers
    ):
        # check if scrobble exists
        scrobble = Scrobble.objects.filter(profile=profile, timestamp=i)
        if scrobble.exists():
            """
            The Audioscrobbler protocol requires us to fail silently here.
            Any response except "OK" would prompt new submission attempts from
            the client. However, if a scrobble with the same profile and
            timestamp is already in the database, this submission will never be
            accepted and the client will try re-submitting indefinitely for as
            long as the submission queue isn't flushed manually. Per protocol,
            only the "OK" response prompts the client to remove a submission
            from the queue.
            """
            continue

        form = ScrobbleForm(
            {
                "profile": profile.pk,
                "timestamp": i,
                "artist_name": a,
                "track_title": t,
                "album_title": b,
                "length": l,
                "tracknumber": n,
            }
        )

        if not form.is_valid():
            return HttpResponseBadRequest("FAILED request invalid")
        else:
            form.save()

    return HttpResponse("OK")
