from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestViewIndex(TestCase):

    def setUp(self):
        self.response = self.client.get(r('index'))

    def test_get(self):
        """GET / must return status_code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, "index.html")
