from rest_framework import status
import pytest
from django.http import HttpRequest
import unittest
from url_shortening_app.utils import generate_random_string
from url_shortening_app.views import encode_url

REDIS_DATA = {}


class FakeRedis:
    """Fake Redis Class for Tests"""

    def __init__(self):
        global REDIS_DATA
        self.data = REDIS_DATA

    def get(self, key):
        return self.data.get(str(key))

    def set_(self, key, value):
        return self.data.set(str(key), value)

    def delete(self, key):
        return self.data.delete(str(key))


@pytest.fixture
def mock_redis(monkeypatch):
    global REDIS_DATA
    REDIS_DATA = {}
    return FakeRedis("")


class UrlEncodeDecodeTests(unittest.TestCase):
    def test_encode_url(self):

        original_url = (
            "https://www.google.com/search?q=build_absolute"
            "_uri&oq=build_absolute_uri&aqs=chrome."
            ".69i57j0i512l2j0i5i30l2j0i5i10i30j0i30j69i61."
            "789j0j7&sourceid=chrome&ie=UTF-8"
        )

        request = HttpRequest()

        request.method = "POST"
        request.POST["original_url"] = original_url
        request.POST["original_url_id"] = generate_random_string()
        request.META["HTTP_HOST"] = "localhost"
        response = encode_url(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
