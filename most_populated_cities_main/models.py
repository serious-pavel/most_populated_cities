from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Country(models.Model):
    class Region(models.TextChoices):
        EUROPE = "EU", _("Europe")
        ASIA = "AS", _("Asia")
        NORTH_AMERICA = "NA", _("North America")
        SOUTH_AMERICA = "SA", _("South America")
        AFRICA = "AF", _("Africa")
        OCEANIA = "OC", _("Oceania")
        ANTARCTICA = "AN", _("Antarctica")

        # def __str__(self):
        #     return f"({self.label})"

    numeric_code = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=False, unique=True)
    alpha2_code = models.CharField(max_length=2, null=False, unique=True)
    alpha3_code = models.CharField(max_length=3, null=False, unique=True)
    official_name = models.CharField(max_length=50, null=False, unique=True)
    common_name = models.CharField(max_length=50, null=False, unique=True)
    region = models.CharField(max_length=2, choices=Region.choices, default=Region.ANTARCTICA, null=False)

    def __str__(self):
        return f"{self.common_name} ({self.region})"


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, unique=True)
    population_23 = models.PositiveIntegerField(null=False)
    population_22 = models.PositiveIntegerField(null=False)

