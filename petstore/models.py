from django.db import models

class Animal(models.Model):
    castrated_options = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )
    species = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
    )
    name = models.CharField(max_length=25)
    species = models.CharField(max_length=25, choices=species)
    age = models.SmallIntegerField()
    city = models.CharField(max_length=35)
    castrated = models.CharField(max_length=12, choices=castrated_options)
    breed = models.CharField(max_length=20)
    cover = models.ImageField()

    def __str__(self):
        return self.name

class Image(models.Model):
    dog = models.ForeignKey(Animal, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')


