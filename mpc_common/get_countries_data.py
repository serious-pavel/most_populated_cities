import csv

with (open('data_files/countries_common_names.csv', mode='r') as csv_common_names,
      open('data_files/countries_by_regions_and_continents.csv', mode='r') as csv_regions,
      open('data_files/countries_data.csv', mode='w', newline='') as csv_counties_data):
    csv_common_names_reader = csv.DictReader(csv_common_names)
    csv_regions_reader = csv.DictReader(csv_regions)

    fields = csv_common_names_reader.fieldnames
    fields.extend(['region', 'continent'])
    csv_countries_writer = csv.DictWriter(csv_counties_data, fieldnames=fields)

    csv_countries_writer.writeheader()
    for row_cn in csv_common_names_reader:
        has_matches = False
        for row_reg in csv_regions_reader:
            if row_cn['id'] == row_reg["M49 Code"]:
                has_matches = True
                row_cn['region'] = row_reg['Region 1']
                row_cn['continent'] = row_reg['Continent']

                if not(row_cn["common_name"] == row_reg["Country or Area"] or
                        row_cn["readable_full_name"] == row_reg["Country or Area"] or
                        row_cn["official_name"] == row_reg["Country or Area"]):
                    print(f'{row_cn["common_name"]}[{row_cn["alpha3"]}] != {row_reg["Country or Area"]}')

                csv_countries_writer.writerow(row_cn)
        if not has_matches:
            print(f'\t{row_cn["common_name"]} ({row_cn["id"]}) has no matches'
                  f'\n{row_cn["id"]},{row_cn["alpha2"]},{row_cn["alpha3"]},"{row_cn["official_name"]}",'
                  f'"{row_cn["common_name"]}","{row_cn["readable_full_name"]}"')
        csv_regions.seek(0)
        next(csv_regions_reader)

    csv_common_names.seek(0)
    next(csv_common_names_reader)

    for row_reg in csv_regions_reader:
        has_matches = False
        if row_reg["ISO-alpha3 Code"]:
            for row_cn in csv_common_names_reader:
                if row_cn['id'] == row_reg["M49 Code"]:
                    has_matches = True
            if not has_matches:
                print(f'\t{row_reg["Country or Area"]} ({row_reg["M49 Code"]}) has no matches'
                      f'\t{row_reg["No"] + 1},{row_cn["common_name"]},{row_cn["alpha3_code"].upper()},'
                      f'{row_cn["numeric_code"]},!add_region1,,!add_continent')
        csv_common_names.seek(0)
        next(csv_common_names_reader)
