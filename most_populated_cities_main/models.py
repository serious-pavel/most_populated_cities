from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Country(models.Model):
    REGION_CHOICES = [
        ("EU", "Europe"),
        ("AS", "Asia"),
        ("NA", "North America"),
        ("SA", "South America"),
        ("AF", "Africa"),
        ("OC", "Oceania"),
        ("AN", "Antarctica"),
    ]
    numeric_code = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=False, unique=True)
    alpha2_code = models.CharField(max_length=2, null=False, unique=True)
    alpha3_code = models.CharField(max_length=3, null=False, unique=True)
    official_name = models.CharField(max_length=50, null=False, unique=True)
    common_name = models.CharField(max_length=50, null=False, unique=True)
    region = models.CharField(max_length=2, choices=REGION_CHOICES, default="AN", null=False)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, unique=True)
    population_23 = models.PositiveIntegerField(null=False)
    population_22 = models.PositiveIntegerField(null=False)

