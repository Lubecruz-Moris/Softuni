from django.core import exceptions


def validate_only_alnumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != "_":
            raise exceptions.ValidationError('Ensure this value contains only letters, numbers and underscore.')