from unittest import TestCase
from django.urls import resolve, reverse
from petstore.views import *


class ViewTest(TestCase):
    def test_home_view_is_correct(self):
        view = resolve(reverse('home'))
        self.assertIs(view.func, home_view)

    def test_one_only_view_is_correct(self):
        view = resolve(reverse('one-only'))
        self.assertIs(view.func, one_only_view)