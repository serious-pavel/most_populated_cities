import csv

with open('data_files/region_codes.csv', mode='r') as csv_reg:
    csv_reg_reader = csv.DictReader(csv_reg)
    # line_count = 0
    for row_reg in csv_reg_reader:
        print(f'{row_reg["Region 1"].upper().replace(" ", "_").replace("-", "_")} = '
              f'"{row_reg["Code"]}", _("{row_reg["Region 1"]}")')

