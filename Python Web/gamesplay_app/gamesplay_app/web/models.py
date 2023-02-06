from enum import Enum

from django.core import validators
from django.db import models


# Create your models here.


class Profile(models.Model):
    MIN_AGE = 12
    MAX_CHAR_LEN = 30
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ),
    )
    password = models.CharField(
        max_length=MAX_CHAR_LEN,
        null=False,
        blank=False,


    )
    first_name = models.CharField(
        max_length=MAX_CHAR_LEN,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_CHAR_LEN,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class GameCategories(ChoicesEnum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'


class Game(models.Model):
    MAX_CHAR_FIELD = 30
    MAX_CATEGORY_FIELD = 15
    MIN_LEVEL = 1
    MIN_RATING = 0.1
    MAX_RATING = 5.0
    title = models.CharField(
        max_length=MAX_CHAR_FIELD,
        null=False,
        blank=False,
        unique=True,
    )
    category = models.CharField(
        max_length=MAX_CATEGORY_FIELD,
        choices=GameCategories.choices(),
        null=False,
        blank=False
    )
    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_RATING),
            validators.MaxValueValidator(MAX_RATING),
        ),
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            validators.MinValueValidator(MIN_LEVEL),
        ),
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
