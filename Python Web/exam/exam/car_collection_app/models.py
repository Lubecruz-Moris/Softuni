from enum import Enum

from django.core import validators
from django.db import models


class Profile(models.Model):
    MAX_LEN_USER = 10
    MIN_LEN_USER = 2
    MIN_AGE = 18
    MAX_GEN_LEN = 30
    MIN_LEN_USER_ERROR_MESSAGE = validators.ValidationError("The username must be a minimum of 2 chars")
    username = models.CharField(
        max_length=MAX_LEN_USER,
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(MIN_LEN_USER, MIN_LEN_USER_ERROR_MESSAGE ),)

    )
    email = models.EmailField(
        null=False,
        blank=False,

    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(validators.MinValueValidator(MIN_AGE),),
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_GEN_LEN,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_GEN_LEN
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_GEN_LEN
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class TypeChoices(ChoicesEnum):
    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"


class Car(models.Model):
    MAX_LEN_TYPE = 10
    MAX_MODEL_LEN = 20
    MIN_MODEL_LEN =2
    MAX_YEAR = 2049
    MIN_YEAR = 1980
    YEAR_OUT_OF_RANGE_MESSAGE = validators.ValidationError("Year must be between 1980 and 2049")
    MIN_PRICE = 1
    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        null=False,
        blank=False,
        choices=TypeChoices.choices(),
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_MODEL_LEN,
        validators=(validators.MinLengthValidator(MIN_MODEL_LEN),),
        )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(validators.MaxValueValidator(MAX_YEAR, YEAR_OUT_OF_RANGE_MESSAGE),
                    validators.MinValueValidator(MIN_YEAR, YEAR_OUT_OF_RANGE_MESSAGE),)
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(validators.MinValueValidator(MIN_PRICE),)
    )