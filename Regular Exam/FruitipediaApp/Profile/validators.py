from django.core.validators import ValidationError


def starts_with_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")

