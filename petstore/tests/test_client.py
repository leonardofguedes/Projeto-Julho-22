import unittest

import pytest
from django.urls import resolve, reverse
from petstore.views.views import *
from django.test import Client


@pytest.mark.django_db(True)
class ClientViewTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_home_returns_status_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_one_only_returns_status_404_with_no_animal_include(self):
        response = self.client.get(reverse('one-only', kwargs={'id':5}))
        self.assertEqual(response.status_code, 404)

