from django.test import TestCase

from url_shortening_app.models import OriginalUrl


class OriginalModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        OriginalUrl.objects.create(
            original_url="www.instagram.com", original_url_id="nt3wa7"
        )

    def test_original_url_label(self):
        original_url = OriginalUrl.objects.get(id=1)
        field_label = original_url._meta.get_field("original_url").verbose_name
        self.assertEqual(field_label, "original url")

    def test_original_url_id_label(self):
        original_url_id = OriginalUrl.objects.get(id=1)
        field_label = original_url_id._meta.get_field(
            "original_url_id"
        ).verbose_name
        self.assertEqual(field_label, "original url id")

    def test_original_url_max_length(self):
        original_url = OriginalUrl.objects.get(id=1)
        max_length = original_url._meta.get_field("original_url").max_length
        self.assertEqual(max_length, 500)

    def test_original_url_id_max_length(self):
        original_url = OriginalUrl.objects.get(id=1)
        max_length = original_url._meta.get_field("original_url_id").max_length
        self.assertEqual(max_length, 10)
