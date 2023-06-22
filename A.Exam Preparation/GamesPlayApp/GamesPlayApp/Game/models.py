from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Game(models.Model):
    title = models.CharField(max_length=30, unique=True)

    category = models.CharField(max_length=15, choices=[
        ("Action", "Action"), ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"), ("Strategy", "Strategy"),
        ("Sports", "Sports"), ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other")
    ])

    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])

    max_level = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)

    image_url = models.URLField()

    summary = models.TextField(blank=True)

