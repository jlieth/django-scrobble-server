from django.test import TestCase
from scrobble_server.api.v12.models import Client


class ClientTests(TestCase):
    def setUp(self):
        self.client_id = "testclient"
        self.client_version = "0.1b2"

    def test_str(self):
        client = Client.objects.create(
            client_id=self.client_id, client_version=self.client_version
        )
        s = "%s@%s" % (self.client_id, self.client_version)
        self.assertEqual(str(client), s)
