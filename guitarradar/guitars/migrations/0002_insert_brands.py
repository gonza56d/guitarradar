import csv

from django.db import migrations, IntegrityError


def _insert_brands(apps, schema_editor):
    Brand = apps.get_model('guitars', 'Brand')
    with open('csv/brands.csv') as file:
        file = csv.reader(file, delimiter=',')
        print(file)
        for index, data in enumerate(file):
            if index == 0:
                continue
            try:
                brand = Brand(name=data[0], url=data[1])
                brand.save()
            except IntegrityError:
                print(f'Brand {brand.name} already exists in database')


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0001_initial')
    ]

    operations = [
        migrations.RunPython(_insert_brands)
    ]
