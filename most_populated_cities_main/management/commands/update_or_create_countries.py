from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Update or Create Countries from csv file'

    def handle(self, *args, **options):
        countries_data_file = "mpc_common/data_files/countries_data.csv"
        if os.path.isfile(countries_data_file):
            print('Processing the countries data file...')
            import csv
            from most_populated_cities_main.models import Country, get_key_name

            with open(countries_data_file, mode='r', encoding='UTF-8') as countries_csv:
                countries_csv_reader = csv.DictReader(countries_csv)
                count = 1
                for row_cn in countries_csv_reader:
                    obj_dict = {
                        'numeric_code': row_cn['id'],
                        'alpha2_code': row_cn['alpha2'],
                        'alpha3_code': row_cn['alpha3'],
                        'official_name': row_cn['readable_full_name'],
                        'common_name': row_cn['common_name'],
                        'continent': Country.Continent[get_key_name(row_cn['continent'])],
                        'region': Country.Region[get_key_name(row_cn['region'])],
                    }
                    obj, created = Country.objects.update_or_create(
                        numeric_code=f"{row_cn['id']}",
                        defaults=obj_dict,
                    )
                    print(f'{count}. {obj} {"created" if created else "updated"}')

                    count += 1

        else:
            print("Countries data file doesn't exist")

