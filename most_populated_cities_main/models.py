from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


def get_key_name(name):
    return name.upper().replace(' ', '_').replace('-', '_')


class Country(models.Model):
    class Continent(models.TextChoices):
        EUROPE = "EU", _("Europe")
        ASIA = "AS", _("Asia")
        NORTH_AMERICA = "NA", _("North America")
        SOUTH_AMERICA = "SA", _("South America")
        AFRICA = "AF", _("Africa")
        OCEANIA = "OC", _("Oceania")
        ANTARCTICA = "AN", _("Antarctica")
        # from most_populated_cities_main.models import Country, get_key_name
        # Country.Region[get_key_name('South-eastern Asia')]

    class Region(models.TextChoices):
        SOUTHERN_ASIA = "S_AS", _("Southern Asia")
        NORTHERN_EUROPE = "N_EU", _("Northern Europe")
        SOUTHERN_EUROPE = "S_EU", _("Southern Europe")
        NORTHERN_AFRICA = "N_AF", _("Northern Africa")
        POLYNESIA = "POLY", _("Polynesia")
        MIDDLE_AFRICA = "M_AF", _("Middle Africa")
        CARIBBEAN = "CARI", _("Caribbean")
        ANTARCTICA = "ANTA", _("Antarctica")
        SOUTH_AMERICA = "S_AM", _("South America")
        WESTERN_ASIA = "W_AS", _("Western Asia")
        AUSTRALIA_AND_NEW_ZEALAND = "A_NZ", _("Australia and New Zealand")
        WESTERN_EUROPE = "W_EU", _("Western Europe")
        EASTERN_EUROPE = "E_EU", _("Eastern Europe")
        CENTRAL_AMERICA = "C_AM", _("Central America")
        WESTERN_AFRICA = "W_AF", _("Western Africa")
        NORTHERN_AMERICA = "N_AM", _("Northern America")
        SOUTHERN_AFRICA = "S_AF", _("Southern Africa")
        EASTERN_AFRICA = "E_AF", _("Eastern Africa")
        SOUTH_EASTERN_ASIA = "SEAS", _("South-eastern Asia")
        EASTERN_ASIA = "E_AS", _("Eastern Asia")
        MELANESIA = "MELA", _("Melanesia")
        MICRONESIA = "MICR", _("Micronesia")
        CENTRAL_ASIA = "C_AS", _("Central Asia")

    numeric_code = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1000)], null=False, unique=True)
    alpha2_code = models.CharField(max_length=2, null=False, unique=True)
    alpha3_code = models.CharField(max_length=3, null=False, unique=True)
    official_name = models.CharField(max_length=50, null=False, unique=True)
    common_name = models.CharField(max_length=50, null=False, unique=True)
    continent = models.CharField(max_length=2, choices=Continent.choices, default=Continent.ANTARCTICA, null=False)
    region = models.CharField(max_length=4, choices=Region.choices, default=Region.ANTARCTICA, null=False)

    @property
    def continent_name(self):
        return self.Continent(self.continent).label

    @property
    def region_name(self):
        return self.Region(self.region).label

    def __str__(self):
        return f"{self.common_name} ({self.continent_name})"

    class Meta:
        verbose_name_plural = "countries"


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, unique=True)
    population_23 = models.PositiveIntegerField(null=False)
    population_22 = models.PositiveIntegerField(null=False)

    class Meta:
        verbose_name_plural = "cities"


def validate_country_continent_and_region(sender, instance, **kwargs):
    from django.core.exceptions import ValidationError

    valid_continent_values = Country.Continent.values
    if instance.continent not in valid_continent_values:
        raise ValidationError(
            f'Country "{instance.common_name}" Continent "{instance.continent}" is not one of the permitted'
            f' values: {", ".join(valid_continent_values)}')
    valid_region_values = Country.Region.values
    if instance.region not in valid_region_values:
        raise ValidationError(
            f'Country "{instance.common_name}" Region "{instance.region}" is not one of the permitted'
            f' values: {", ".join(valid_region_values)}')


models.signals.pre_save.connect(validate_country_continent_and_region, sender=Country)

