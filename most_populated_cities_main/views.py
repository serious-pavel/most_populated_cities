from django.shortcuts import render
from .models import Country, City
from django.core.paginator import Paginator

# Create your views here.


def city_page(request):
    cities = City.objects.all()
    return render(request, 'most_populated_cities_main/table_cities.html', context={'cities': cities})


def country_page(request):
    countries = Country.objects.all().order_by('common_name')
    per_page = request.GET.get("choice")
    if not per_page:
        per_page = "20"
    paginator = Paginator(countries, per_page)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    item_counter = (page_obj.number - 1) * paginator.per_page

    return render(request, 'most_populated_cities_main/table_countries.html',
                  context={'page_obj': page_obj, 'item_counter': item_counter, 'per_page': per_page})
