from django.db import models


class Profile(models.Model):
    MAX_LEN = 30
    first_name = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )


class Book(models.Model):
    MAX_LEN = 30
    title = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    type = models.CharField(
        max_length=MAX_LEN,
        null=False,
        blank=False,
    )