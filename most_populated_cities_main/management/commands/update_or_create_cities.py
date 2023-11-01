from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Update or Create Countries from csv file'

    def handle(self, *args, **options):
        cities_data_file = "mpc_common/data_files/most_populated_cities.csv"
        if os.path.isfile(cities_data_file):
            print('Processing the cities data file...')
            import csv
            from most_populated_cities_main.models import Country, City

            with open(cities_data_file, mode='r', encoding='UTF-8') as cities_csv:
                countries_csv_reader = csv.DictReader(cities_csv)
                count = 1
                for row_ct in countries_csv_reader:
                    obj_dict = {
                        'country': Country.objects.get(common_name=row_ct['Country']),
                        'name': row_ct['City'],
                        'population_23': row_ct['Pop2023'],
                        'population_22': row_ct['Pop2022'],
                    }

                    obj, created = City.objects.update_or_create(
                        name=f"{row_ct['City']}",
                        defaults=obj_dict,
                    )
                    print(f'{count}. {obj} {"created" if created else "updated"}')

                    count += 1

        else:
            print("Countries data file doesn't exist")

