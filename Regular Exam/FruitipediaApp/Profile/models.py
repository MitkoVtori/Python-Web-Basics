from django.db import models
from django.core.validators import MinLengthValidator
from FruitipediaApp.Profile.validators import starts_with_letter


class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=[MinLengthValidator(2), starts_with_letter])

    last_name = models.CharField(max_length=35, validators=[MinLengthValidator(1), starts_with_letter])

    email = models.EmailField(max_length=40)

    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])

    image_url = models.URLField(blank=True, null=True)

    age = models.IntegerField(default=18, blank=True)

