from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


class Profile(models.Model):
    username = models.CharField(validators=[MinLengthValidator(
        2,
        message="The username must be a minimum of 2 chars")],
        max_length=10,
        blank=False
    )

    email = models.EmailField(blank=False)

    age = models.IntegerField(validators=[MinValueValidator(18)], blank=False)

    password = models.CharField(max_length=30, blank=False)

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    profile_picture = models.URLField(blank=True)

