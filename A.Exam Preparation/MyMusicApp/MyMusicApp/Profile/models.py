from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from MyMusicApp.MyMusicApp.Profile.validators import valid_username


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(2), valid_username])

    email = models.EmailField()

    age = models.IntegerField(validators=[MinValueValidator(0)], blank=True)

