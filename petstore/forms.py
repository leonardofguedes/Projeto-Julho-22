from django.forms import ModelForm
from .models import Animal, Image
from django import forms


class AnimalForm(ModelForm):
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


