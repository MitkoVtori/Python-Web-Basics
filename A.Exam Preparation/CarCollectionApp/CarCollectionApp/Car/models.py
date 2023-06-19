from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class Car(models.Model):
    type = models.CharField(max_length=10, choices=[
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    ], blank=False)

    model = models.CharField(max_length=20, validators=[MinLengthValidator(2)], blank=False)

    year = models.IntegerField(validators=[MinValueValidator(
        1980,
        message="Year must be between 1980 and 2049"
    ), MaxValueValidator(
        2049,
        message="Year must be between 1980 and 2049")],
        blank=False)

    image_url = models.URLField(blank=False)

    price = models.FloatField(validators=[MinValueValidator(1)], blank=False)