from django.core.exceptions import ValidationError


def min_length_validator(value):
    if len(value) < 2:
        raise ValidationError("Name is too short!")


def max_length_validator(value):
    if len(value) > 30:
        raise ValidationError("Name is too long!")

