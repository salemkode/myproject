from django.test import TestCase


class ProductHeadlessViewTests(TestCase):
    def test_home_headless_view_returns_json(self):
        response = self.client.get("/products/api/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"page": "home", "title": "Welcome"})

    def test_about_headless_view_returns_json(self):
        response = self.client.get("/products/api/about/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"page": "about", "title": "About"})
