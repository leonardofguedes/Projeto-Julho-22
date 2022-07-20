from unittest import TestCase
from clients.forms.register_form import RegisterForm
from django.test import TestCase as DjangoTestCase
from django.urls import reverse
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Username'),
        ('email', 'Seu e-mail'),
        ('first_name', 'Ex: Pedro'),
        ('last_name', 'Ex: Silva'),
        ('password', 'Sua senha'),
        ('password2', 'Repita a senha'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('username', (
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        )),
        ('email', 'O email precisa ser válido'),
        ('password', (
                'A senha precisa de uma letra maiúscula, uma minúscula e um número.Ela não '
                'pode ter menos que 8 caracteres'
        )),
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

    @parameterized.expand([
        ('username', 'Username'),
        ('first_name', 'Primeiro nome'),
        ('last_name', 'Último nome'),
        ('email', 'E-mail'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anyemail.com',
            'password': '1',
            'password2': '1',
        }
        return super().setUp(*args, **kwargs)
