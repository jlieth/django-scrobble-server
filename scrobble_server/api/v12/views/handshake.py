import calendar
import hashlib
import sys

from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET

from scrobble_server.core.models.profile import Profile
from scrobble_server.api.v12.decorators import required_params
from scrobble_server.api.v12.models import Client, ScrobbleSession

User = get_user_model()


@require_GET
@required_params(["hs", "p", "c", "v", "u", "t", "a"])
def handshake(request):
    # extract params
    hs = request.GET.get("hs")
    protocol = request.GET.get("p")
    client_id = request.GET.get("c")
    client_version = request.GET.get("v")
    username = request.GET.get("u")
    timestamp = request.GET.get("t")
    auth = request.GET.get("a")

    # validate params
    if not hs == "true":
        return HttpResponseBadRequest("FAILED 'hs' has to be true")

    if not protocol == "1.2":
        return HttpResponseBadRequest(
            "FAILED This endpoint supports protocol v1.2 only."
        )

    if not timestamp.isdigit():
        return HttpResponseBadRequest("BADTIME")

    # difference submitted timestamp and real timestamp
    if sys.version_info.major == 2:
        timediff = calendar.timegm(timezone.now().timetuple()) - int(timestamp)
    else:
        timediff = timezone.now().timestamp() - int(timestamp)
    if abs(timediff) > 86400:
        return HttpResponseBadRequest("BADTIME")

    # get user
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponseBadRequest("BADAUTH")

    # check auth
    try:
        md5hash = user.profile.md5hash.hash
    except Profile.md5hash.RelatedObjectDoesNotExist:
        return HttpResponseBadRequest(
            "FAILED You need to set up your account for this protocol"
        )

    auth_string = (md5hash + timestamp).encode("utf-8")
    auth_expected = hashlib.md5(auth_string).hexdigest()
    if not auth == auth_expected:
        return HttpResponseBadRequest("BADAUTH")

    # check client
    client, created = Client.objects.update_or_create(
        client_id=client_id,
        client_version=client_version,
        defaults={"last_seen": timezone.now()},
    )
    if client.banned:
        return HttpResponseBadRequest("BANNED")

    # create a scrobble session
    session = ScrobbleSession.objects.create(profile=user.profile, client=client)
    session_id = session.key

    # build response
    nowplaying_path = reverse("api_v1.2:nowplaying")
    submission_path = reverse("api_v1.2:scrobble")
    nowplaying = request.build_absolute_uri(nowplaying_path)
    submission = request.build_absolute_uri(submission_path)

    response = "OK\n{}\n{}\n{}".format(session_id, nowplaying, submission)
    return HttpResponse(response)
