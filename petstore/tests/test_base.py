from django.test import TestCase
from petstore.models import Animal, User

class TestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_author(self,
                    first_name='Usuário Teste',
                    last_name='Sobrenome Teste',
                    username='Username Teste',
                    password='123456teste',
                    email='teste@gmail.com',
                    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,)

    def make_animal(self,
                    name='Animal Teste Name',
                    species='Cachorro',
                    age='8',
                    city='Cidade Teste',
                    castrated='Sim',
                    breed='Raça Teste',
                    author_info=None
                    ):
        if author_info is None:
            author_info = {}

        return Animal.objects.create(
            id=220790,
            author=self.make_author(**author_info),
            name=name,
            species=species,
            age=age,
            city=city,
            castrated=castrated,
            breed=breed
        )