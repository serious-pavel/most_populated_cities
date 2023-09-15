from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'most_populated_cities_main/table_cities.html')

