from django.test import TestCase
from django.urls import reverse


class PetStoreURLTest(TestCase):
    def test_url_home(self):
        home_url = reverse('register')
        self.assertEqual(home_url, '/users/register/')