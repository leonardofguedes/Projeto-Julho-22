import pytest
from django.urls import resolve, reverse
from petstore.views.views import *
from django.test import Client
from petstore.tests.test_base import TestBase

@pytest.mark.django_db(True)
class ClientViewTest(TestBase):
    def setUp(self) -> None:
        self.client = Client()

    def test_home_returns_status_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_shows_with_animal_registered(self):
        name_home_test = 'Nome Teste Home'
        self.make_animal(name=name_home_test)
        response = self.client.get(reverse('home'))
        content = response.content.decode('utf-8')
        self.assertIn(name_home_test, content)

    def test_one_only_returns_status_404_with_no_animal_include(self):
        response = self.client.get(reverse('one-only', kwargs={'id':5}))
        self.assertEqual(response.status_code, 404)

    def test_one_only_status_with_animal_include(self):
        animal = self.make_animal()
        response = self.client.get(reverse('one-only', kwargs={'id':220790}))
        self.assertEqual(response.status_code, 200)

    def test_one_only_loads_animal_name(self):
        name_test = 'Nome do Teste'
        self.make_animal(name=name_test)
        response = self.client.get(reverse('one-only', kwargs={'id': 220790}))
        content = response.content.decode('utf-8')
        self.assertIn(name_test, content)


