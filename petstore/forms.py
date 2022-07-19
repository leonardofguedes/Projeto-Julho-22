from django.forms import ModelForm
from collections import defaultdict
from django import forms
from django.core.exceptions import ValidationError
from .models import Animal
from clients.forms.django_forms import add_attr
from clients.forms.strings import is_positive_number


class AnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    class Meta:
        model = Animal
        fields = [
            'name',
            'species',
            'age',
            'city',
            'castrated',
            'breed',
            'cover',
        ]


    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 5:
            self._my_errors['name'].append('Precisa ter no mínimo 5 letras.')

        return name

    def clean_age(self):
        field_name = 'age'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('A idade precisa ser um número positivo.')

        return field_value



