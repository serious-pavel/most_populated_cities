from django.shortcuts import render
from .models import Country, City
from django.core.paginator import Paginator

# Create your views here.


def city_page(request):
    sort_by = request.GET.get("sort_by") or "-population_23"

    filter_data = request.GET.get("filter_data") or ""
    index = request.GET.get("index")
    page_number = request.GET.get("page")
    per_page = request.GET.get("per_page") or "15"

    cities = City.objects.all().order_by(sort_by).filter(name__contains=filter_data)

    paginator = Paginator(cities, per_page)

    if index:
        for i in range(1, paginator.num_pages + 1):
            if int(index) < i * int(per_page):
                page_number = str(i)
                break

    page_obj = paginator.get_page(page_number)
    item_counter = (page_obj.number - 1) * paginator.per_page

    per_page_options = sorted([10, 15, 20])
    return render(request, 'most_populated_cities_main/table_cities.html',
                  context={'page_obj': page_obj, 'item_counter': item_counter,
                           'per_page': per_page, 'sort_by': sort_by,
                           'per_page_options': per_page_options, 'filter_data': filter_data})


def country_page(request):
    sort_by = request.GET.get("sort_by") or "common_name"
    filter_data = request.GET.get("filter_data") or ""
    index = request.GET.get("index")
    page_number = request.GET.get("page")
    per_page = request.GET.get("per_page") or "15"

    countries = Country.objects.all().order_by(sort_by).filter(common_name__contains=filter_data)
    paginator = Paginator(countries, per_page)

    if index:
        for i in range(1, paginator.num_pages + 1):
            if int(index) < i * int(per_page):
                page_number = str(i)
                break

    page_obj = paginator.get_page(page_number)
    item_counter = (page_obj.number - 1) * paginator.per_page

    per_page_options = sorted([10, 15, 20])
    return render(request, 'most_populated_cities_main/table_countries.html',
                  context={'page_obj': page_obj, 'item_counter': item_counter,
                           'per_page': per_page, 'sort_by': sort_by,
                           'per_page_options': per_page_options, 'filter_data': filter_data})
