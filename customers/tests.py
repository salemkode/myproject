import json

from django.test import TestCase

from .models import Customer


class CustomerHeadlessApiTests(TestCase):
    def test_can_create_and_list_customers(self):
        response = self.client.post(
            "/customers/api/",
            data=json.dumps({"name": "Ali", "phone_number": "12345"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["customer"]["name"], "Ali")

        response = self.client.get("/customers/api/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "customers": [
                    {"id": 1, "name": "Ali", "phone_number": "12345"},
                ]
            },
        )

    def test_can_get_update_patch_and_delete_customer(self):
        customer = Customer.objects.create(name="Sara", phone_number="777")

        response = self.client.get(f"/customers/api/{customer.id}/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["customer"]["name"], "Sara")

        response = self.client.put(
            f"/customers/api/{customer.id}/",
            data=json.dumps({"name": "Sara Ahmed", "phone_number": "888"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["customer"]["phone_number"], "888")

        response = self.client.patch(
            f"/customers/api/{customer.id}/",
            data=json.dumps({"name": "Sara Updated"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["customer"]["name"], "Sara Updated")

        response = self.client.delete(f"/customers/api/{customer.id}/")

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Customer.objects.filter(id=customer.id).exists())

    def test_create_requires_customer_fields(self):
        response = self.client.post(
            "/customers/api/",
            data=json.dumps({"name": "Missing Phone"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["errors"],
            {"fields": ["Missing fields: phone_number"]},
        )
