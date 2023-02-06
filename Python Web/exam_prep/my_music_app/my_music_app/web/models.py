from enum import Enum
from django.core import validators
from django.db import models

from my_music_app.web.validators import validate_only_alnumeric


# Create your models here.
class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(USERNAME_MIN_LEN),
            validate_only_alnumeric

        ),

    )
    email = models.EmailField(
        null=False,
        blank=False,

    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,

    )


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    POP = 'Pop Music'
    ROCK = 'Rock Music'
    RNB = 'R&B Music'
    JAZZ = 'Jazz Music'
    COUNTRY = 'Country Music'
    DANCE = "Dance Music"
    HIP_HOP = 'Hip-Hop Music'
    OTHER = 'Other'

class Album(models.Model):
    ALBUM_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    album = models.CharField(
        verbose_name="Album Name",
        unique=True,
        max_length=ALBUM_MAX_LEN,
        null=False,
        blank=False
    )
    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
        null=False,
        blank=False
    )
    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=AlbumGenres.choices(),
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        ),


    )
    class Meta:
        ordering= ('pk',)
