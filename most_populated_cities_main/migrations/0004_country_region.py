# Generated by Django 4.2.5 on 2023-10-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('most_populated_cities_main', '0003_alter_city_options_alter_country_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.CharField(choices=[('S_AS', 'Southern Asia'), ('N_EU', 'Northern Europe'), ('S_EU', 'Southern Europe'), ('N_AF', 'Northern Africa'), ('POLY', 'Polynesia'), ('M_AF', 'Middle Africa'), ('CARI', 'Caribbean'), ('ANTA', 'Antarctica'), ('S_AM', 'South America'), ('W_AS', 'Western Asia'), ('A_NZ', 'Australia and New Zealand'), ('W_EU', 'Western Europe'), ('E_EU', 'Eastern Europe'), ('C_AM', 'Central America'), ('W_AF', 'Western Africa'), ('N_AM', 'Northern America'), ('S_AF', 'Southern Africa'), ('E_AF', 'Eastern Africa'), ('SEAS', 'South-eastern Asia'), ('E_AS', 'Eastern Asia'), ('MELA', 'Melanesia'), ('MICR', 'Micronesia'), ('C_AS', 'Central Asia')], default='ANTA', max_length=4),
        ),
    ]
