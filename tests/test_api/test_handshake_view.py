import copy
import hashlib
import time

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse

from scrobble_server.core.models.profile import Profile
from scrobble_server.api.v12.models import Client, ScrobbleSession

User = get_user_model()


class HandshakeTests(TestCase):
    fixtures = ["user_and_profile", "api_v12"]

    def setUp(self):
        self.handshake_url = reverse("api_v1.2:handshake")
        self.user = User.objects.first()
        self.profile = Profile.objects.first()
        self.api_client = Client.objects.first()

    def test_required_params(self):
        # BadRequest when a param is missing from request
        for param in self.request_dict.keys():
            request_dict_copy = copy.copy(self.request_dict)
            del request_dict_copy[param]
            response = self.client.get(self.handshake_url, request_dict_copy)
            self.assertEqual(response.status_code, 400)
            expected_msg = "FAILED missing params in request: {}".format(param)
            self.assertTrue(response.content.decode(), expected_msg)

    def test_param_hs(self):
        # BadRequest when hs != 'true'
        request_dict = self.request_dict
        request_dict["hs"] = "any value but 'true'"
        response = self.client.get(self.handshake_url, request_dict)
        self.assertEqual(response.status_code, 400)
        self.assertTrue(response.content.decode().startswith("FAILED"))

    def test_param_p(self):
        # BadRequest when p != '1.2'
        request_dict = self.request_dict
        request_dict["p"] = "weird protocol version"
        response = self.client.get(self.handshake_url, request_dict)
        self.assertEqual(response.status_code, 400)
        self.assertTrue(response.content.decode().startswith("FAILED"))

    def test_param_t(self):
        # BadRequest when timestamp isn't a digit
        request_dict = self.request_dict
        request_dict["t"] = "not a timestamp"
        response = self.client.get(self.handshake_url, request_dict)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "BADTIME")

        # BadRequest when timestamp is off by too much. Protocol doesn't say
        # how much is too much, but view function says 86400s=24h difference
        request_dict = self.request_dict
        request_dict["t"] = int(time.time()) - 86401
        response = self.client.get(self.handshake_url, request_dict)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "BADTIME")

    def test_nonexistent_user(self):
        # BadRequest when username doesn't exist
        request_dict = self.request_dict
        request_dict["u"] = "I don't exist"
        response = self.client.get(self.handshake_url, request_dict)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "BADAUTH")

    def test_wrong_auth_token(self):
        # BadRequest when username doesn't exist
        request_dict = self.request_dict
        request_dict["a"] = "wrong auth token"
        response = self.client.get(self.handshake_url, request_dict)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "BADAUTH")

    def test_handshake_with_banned_client(self):
        # BadRequest when client is banned
        self.api_client.banned = True
        self.api_client.save()
        response = self.client.get(self.handshake_url, self.request_dict)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "BANNED")

    def test_valid_request(self):
        # Finally, the valid request
        response = self.client.get(self.handshake_url, self.request_dict)
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        self.assertTrue(content.startswith("OK\n"))

        content = content.split("\n")
        self.assertEqual(len(content), 4)
        _, session_id, nowplaying_url, scrobble_url = content

        # need a request object to use request.build_absolute_uri()
        factory = RequestFactory()
        request = factory.get(self.handshake_url, self.request_dict)

        nowplaying_path = reverse("api_v1.2:nowplaying")
        nowplaying = request.build_absolute_uri(nowplaying_path)
        self.assertEqual(nowplaying_url, nowplaying)

        scrobble_path = reverse("api_v1.2:scrobble")
        scrobble = request.build_absolute_uri(scrobble_path)
        self.assertEqual(scrobble_url, scrobble)

    def test_valid_request_creates_new_scrobbling_session(self):
        # no scrobble sessions yet
        self.assertEqual(ScrobbleSession.objects.count(), 0)

        # make request
        self.client.get(self.handshake_url, self.request_dict)

        # should be one session now
        self.assertEqual(ScrobbleSession.objects.count(), 1)

        session = ScrobbleSession.objects.first()
        self.assertEqual(session.profile, self.profile)
        self.assertEqual(session.client, self.api_client)

    @property
    def request_dict(self):
        timestamp = int(time.time())
        auth = "{}{}".format(self.profile.md5hash.hash, timestamp)
        auth = hashlib.md5(auth.encode("utf-8")).hexdigest()
        return {
            "hs": "true",
            "p": "1.2",
            "c": self.api_client.client_id,
            "v": self.api_client.client_version,
            "u": self.user.username,
            "t": timestamp,
            "a": auth,
        }
