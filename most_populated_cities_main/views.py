from django.shortcuts import render
from .models import Country, City

# Create your views here.


def city_page(request):
    cities = City.objects.all()
    return render(request, 'most_populated_cities_main/table_cities.html', context={'cities': cities})


def country_page(request):
    countries = Country.objects.all()
    return render(request, 'most_populated_cities_main/table_countries.html', context={'countries': countries})
