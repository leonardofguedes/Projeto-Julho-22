from django.test import TestCase
from django.urls import reverse


class PetStoreURLTest(TestCase):
    def test_url_home(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')

    def test_url_one_only(self):
        one_only = reverse('one-only')
        self.assertEqual(one_only, '/pet/')

    def test_url_pet_add(self):
        pet_add = reverse('pet-register')
        self.assertEqual(pet_add, '/pet/pet-add/')
