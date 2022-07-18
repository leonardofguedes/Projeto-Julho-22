from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .django_forms import add_placeholder, add_attr, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['first_name'], 'Ex: Pedro')
        add_placeholder(self.fields['last_name'], 'Ex: Silva')
        add_placeholder(self.fields['username'], 'Username')
        add_placeholder(self.fields['email'], 'Seu e-mail')

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Sua senha'
        }),
        error_messages={
            'required': 'A senha pode não ser vazia'
        },
        help_text=(
            'A senha precisa de uma letra maiúscula, uma minúscula e um número.'
            'Ela não pode ter menos que 8 caracteres'
        ),
        validators=[strong_password]
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita a senha'
        })
    )


    class Meta:
        model= User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            ]
        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'username': 'Username',
            'email': 'E-mail',
            'password': 'Senha',
        }
        help_texts = {
            'email': 'O email precisa ser válido'
        }
        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }
        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Digite sua senha aqui'
            })
        }

    def clean_password(self):
        data = self.cleaned_data.get('password')
        if 'atenção' in data:
            raise ValidationError(
                'Não digite %(pipoca)s no campo password',
                code='invalid',
                params={'pipoca': '"atenção"'}
            )
        return data

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if 'John Doe' in data:
            raise ValidationError(
                'Não digite %(value)s no campo first name',
                code='invalid',
                params={'value': '"John Doe"'}
            )
        return data


    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email


    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'Password and password2 must be equal',
                code='invalid'
            )
            raise ValidationError({
                'password': password_confirmation_error,
                'password2': [
                    password_confirmation_error,
                ],
            })

