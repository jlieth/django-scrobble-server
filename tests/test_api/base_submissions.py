from scrobble_server.core.models.profile import Profile
from scrobble_server.api.v12.models import Client, ScrobbleSession


class BaseSubmission:
    fixtures = ["user_and_profile", "api_v12"]

    def setUp(self):
        self.profile = Profile.objects.first()
        self.api_client = Client.objects.first()
        self.session_id = self.create_session()

        self.artist_name = "artist name"
        self.track_title = "track title"
        self.album_title = "album title"
        self.length = 240
        self.tracknumber = 1

    def create_session(self):
        session = ScrobbleSession.objects.create(
            profile=self.profile, client=self.api_client
        )

        return session.key

    def expect_200_OK(self, data):
        response = self.client.post(self.url, data)
        self.assertEqual(response.content.decode(), "OK")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "OK")

    def expect_400_BADSESSION(self, data):
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode(), "BADSESSION")

    def expect_400_FAILED(self, data):
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)
        self.assertTrue(response.content.decode().startswith("FAILED"))

    def test_required_args(self):
        # BadRequest when a param is missing from request
        for param in self.required_params:
            request_dict = self.request_dict
            del request_dict[param]
            self.expect_400_FAILED(request_dict)

    def test_invalid_session(self):
        # invalid session_id should yield status_code=400 and BADSESSION
        request_dict = self.request_dict
        request_dict["s"] = "invalid"
        self.expect_400_BADSESSION(request_dict)

    def test_empty_artist_name(self):
        # empty artist_name should yield status_code=400 and FAILED [...]
        self.artist_name = ""
        self.expect_400_FAILED(self.request_dict)

    def test_empty_track_title(self):
        # empty track_title should yield status_code=400 and FAILED [...]
        self.track_title = ""
        self.expect_400_FAILED(self.request_dict)

    def test_negative_length(self):
        # negative length should yield status_code=400 and FAILED [...]
        self.length = -1
        self.expect_400_FAILED(self.request_dict)

    def test_negative_tracknumber(self):
        # negative tracknumber should yield status_code=400 and FAILED [...]
        self.tracknumber = -1
        self.expect_400_FAILED(self.request_dict)

    def test_valid_request(self):
        # valid request should yield status_code=200 and OK
        self.expect_200_OK(self.request_dict)

    @property
    def request_dict(self):
        raise NotImplementedError()
