import csv

with (open('data_files/most_populated_cities.csv', mode='r') as csv_cities,
      open('data_files/countries_data.csv', mode='r') as csv_countries,
      ):
    csv_cities_reader = csv.DictReader(csv_cities)
    csv_countries_reader = csv.DictReader(csv_countries)

    countries_without_matches = []
    for row_ct in csv_cities_reader:

        has_matches = False
        country = row_ct['Country']
        for row_cn in csv_countries_reader:
            country_cn = row_cn["common_name"]
            if country == country_cn:
                has_matches = True

        if not has_matches:
            if country not in countries_without_matches:
                countries_without_matches.append(country)
                print(f'\t{country} has no matches')
        csv_countries.seek(0)
        next(csv_countries_reader)

