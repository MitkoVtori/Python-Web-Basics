from django.core.validators import MinLengthValidator
from django.db import models
from FruitipediaApp.Fruit.validators import only_letters


class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(2), only_letters])

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(blank=True)

