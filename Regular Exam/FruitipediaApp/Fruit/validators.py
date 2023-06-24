from django.core.validators import ValidationError


def only_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")

