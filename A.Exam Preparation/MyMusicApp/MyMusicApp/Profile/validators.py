from django.core.validators import ValidationError


def valid_username(value):
    for char in value:
        if not char.isalnum() and char != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

