from unittest import TestCase
from django.urls import resolve, reverse
from clients.views.all import *
from clients.views.dashboard import *


class ViewTest(TestCase):
    def test_register_view_is_correct(self):
        view = resolve(reverse('register'))
        self.assertIs(view.func, register_view)

    def test_register_create_view_is_correct(self):
        view = resolve(reverse('create'))
        self.assertIs(view.func, register_create)

    def test_login_view_is_correct(self):
        view = resolve(reverse('login'))
        self.assertIs(view.func, login_view)

    def test_login_create_view_is_correct(self):
        view = resolve(reverse('login_create'))
        self.assertIs(view.func, login_create)

    def test_logout_view_is_correct(self):
        view = resolve(reverse('logout'))
        self.assertIs(view.func, logout_view)

    def test_dash_view_is_correct(self):
        view = resolve(reverse('dashboard'))
        self.assertIs(view.func, dashboard)

    def test_dash_new_animal_view_is_correct(self):
        view = resolve(reverse('dashboard-animal-new'))
        self.assertIs(view.func.view_class, Dashboard)

    def test_dash_animal_delete_view_is_correct(self):
        view = resolve(reverse('dashboard-animal-delete'))
        self.assertIs(view.func.view_class, Dashboard_Delete)

    def test_dash_animal_edit_view_is_correct(self):
        view = resolve(reverse('dashboard-edit', kwargs={'id':5000}))
        self.assertIs(view.func.view_class, Dashboard)
