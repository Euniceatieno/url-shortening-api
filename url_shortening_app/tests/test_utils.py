import unittest
from url_shortening_app.utils import (
    generate_random_string,
    validate_url,
)


class RandomStringGeneratorTest(unittest.TestCase):
    def test_generate_random_string(self):
        random_string = generate_random_string()
        self.assertEqual(len(random_string), 6)
        self.assertEqual(type(random_string), str)


class ValidateURLTest(unittest.TestCase):
    def test_validate_url(self):
        test_url = (
            "https://www.google.com/search?q=build_absolute"
            "_uri&oq=build_absolute_uri&aqs=chrome."
            ".69i57j0i512l2j0i5i30l2j0i5i10i30j0i30j69i61."
            "789j0j7&sourceid=chrome&ie=UTF-8"
        )
        response = validate_url(test_url)
        self.assertEqual(response, True)
