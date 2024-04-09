from django.shortcuts import render
from .models import Country, City
from django.core.paginator import Paginator

# Create your views here.


def render_paginated_table(request, queryset, template_name, filter_field, default_sort_by):
    sort_by = request.GET.get("sort_by", default_sort_by)
    filter_data = request.GET.get("filter_data", "")
    index = request.GET.get("index")
    page_number = request.GET.get("page")
    per_page = request.GET.get("per_page", "15")

    objects = queryset.order_by(sort_by).filter(**{filter_field + '__contains': filter_data})
    paginator = Paginator(objects, per_page)

    if index:
        for i in range(1, paginator.num_pages + 1):
            if int(index) < i * int(per_page):
                page_number = str(i)
                break

    page_obj = paginator.get_page(page_number)
    item_counter = (page_obj.number - 1) * paginator.per_page

    per_page_options = sorted([10, 15, 20])
    return render(request, template_name,
                  context={'page_obj': page_obj, 'item_counter': item_counter,
                           'per_page': per_page, 'sort_by': sort_by,
                           'per_page_options': per_page_options, 'filter_data': filter_data})


def city_page(request):
    cities = City.objects.all()
    return render_paginated_table(request, cities, 'most_populated_cities_main/table_cities.html',
                                  'name', '-population_23')


def country_page(request):
    countries = Country.objects.all()
    return render_paginated_table(request, countries, 'most_populated_cities_main/table_countries.html',
                                  'common_name', 'common_name')
