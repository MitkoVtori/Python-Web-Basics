from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from . import validators


class Developer(models.Model):
    first_name = models.CharField(max_length=30, validators=[MaxLengthValidator(30), validators.min_length_validator])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(2), validators.max_length_validator])
    developer_id = models.PositiveIntegerField(unique=True, error_messages={"unique": "ID already registered!"})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

