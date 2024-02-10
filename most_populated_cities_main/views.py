from django.shortcuts import render
from .models import Country, City
from django.core.paginator import Paginator

# Create your views here.


def city_page(request):
    cities = City.objects.all()
    return render(request, 'most_populated_cities_main/table_cities.html', context={'cities': cities})


def country_page(request):
    sort_by = request.GET.get("sort_by") or "common_name"
    filter_data = request.GET.get("filter_data") or ""
    countries = Country.objects.all().order_by(sort_by).filter(common_name__contains=filter_data)

    per_page = request.GET.get("per_page") or "15"
    paginator = Paginator(countries, per_page)

    index = request.GET.get("index")
    page_number = request.GET.get("page")
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
