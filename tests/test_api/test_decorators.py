from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.test import TestCase

from scrobble_server.api.v12.decorators import required_params

User = get_user_model()


def dummy_function(request, *args, **kwargs):
    return HttpResponse("Dummy response")


class RequiredParamsTests(TestCase):
    def setUp(self):
        self.decorator = required_params
        self.func = dummy_function

    @staticmethod
    def create_request(method, params):
        request = HttpRequest()
        request.method = method
        if method == "POST":
            request.POST.update(params)
        else:
            request.GET.update(params)
        return request

    def test_nothing_required_nothing_given(self):
        required = []

        for method in ["GET", "POST"]:
            request = self.create_request(method, {})
            response = self.decorator(required)(self.func)(request)
            self.assertEqual(response.status_code, 200)

    def test_nothing_required_something_given(self):
        required = []

        for method in ["GET", "POST"]:
            request = self.create_request(method, {"something": "given"})
            response = self.decorator(required)(self.func)(request)
            self.assertEqual(response.status_code, 200)

    def test_something_required_nothing_given(self):
        required = ["something", "or", "other"]

        for method in ["GET", "POST"]:
            request = self.create_request(method, {})
            response = self.decorator(required)(self.func)(request)
            self.assertEqual(response.status_code, 400)

    def test_something_required_something_given(self):
        required = ["something", "or", "other"]

        for method in ["GET", "POST"]:
            request = self.create_request(
                method, {"something": "foo", "or": "bar", "other": "baz"}
            )
            response = self.decorator(required)(self.func)(request)
            self.assertEqual(response.status_code, 200)
