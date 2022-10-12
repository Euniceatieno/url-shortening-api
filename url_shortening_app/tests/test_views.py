from rest_framework import status
from rest_framework.test import APITestCase


class UrlEncodeDecodeTests(APITestCase):
    def test_encode_url(self):
        original_url = (
            "https://www.google.com/search?q=build_absolute"
            "_uri&oq=build_absolute_uri&aqs=chrome."
            ".69i57j0i512l2j0i5i30l2j0i5i10i30j0i30j69i61."
            "789j0j7&sourceid=chrome&ie=UTF-8"
        )
        original_url_id = "nt3wa7"

        data = {
            "original_url": original_url,
            "original_url_id": original_url_id,
        }
        response = self.client.post("/encode_url/", data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_decode_url(self):

        data = {"shortened_url": "http://127.0.0.1:8000/nt3wa7"}
        response = self.client.post("/decode_url/", data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
