from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Country(models.Model):
    class Continent(models.TextChoices):
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
    continent = models.CharField(max_length=2, choices=Continent.choices, default=Continent.ANTARCTICA, null=False)

    @property
    def continent_name(self):
        return self.Continent(self.continent).label

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


def validate_country_continent(sender, instance, **kwargs):
    valid_values = Country.Continent.values
    if instance.continent not in valid_values:
        from django.core.exceptions import ValidationError
        raise ValidationError(
            f'Country "{instance.common_name}" Region "{instance.continent}" is not one of the permitted'
            f' values: {", ".join(valid_values)}')


models.signals.pre_save.connect(validate_country_continent, sender=Country)

