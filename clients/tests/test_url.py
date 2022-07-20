from django.test import TestCase
from django.urls import reverse


class ClientsURLTest(TestCase):
    def test_url_register(self):
        register_url = reverse('register')
        self.assertEqual(register_url, '/users/register/')

    def test_url_login(self):
        login_url = reverse('login')
        self.assertEqual(login_url, '/users/login/')

    def test_url_logout(self):
        logout_url = reverse('logout')
        self.assertEqual(logout_url, '/users/logout/')

    def test_url_dashboard(self):
        dashboard_url = reverse('dashboard')
        self.assertEqual(dashboard_url, '/users/dashboard/')

    def test_url_dashboard_new(self):
        dashboard_url_new = reverse('dashboard-animal-new')
        self.assertEqual(dashboard_url_new, '/users/dashboard/animal/new/')

    def test_url_dashboard_delete(self):
        dashboard_url_delete = reverse('dashboard-animal-delete')
        self.assertEqual(dashboard_url_delete, '/users/dashboard/animal/delete/')

    def test_url_dashboard_edit(self):
        dashboard_url_edit = reverse('dashboard-edit', kwargs={'id': 5000})
        self.assertEqual(dashboard_url_edit, '/users/dashboard/animal/5000/edit/')
