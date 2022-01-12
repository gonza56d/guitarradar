import csv

from django.db import migrations, IntegrityError


def _insert_bridges(apps, schema_editor):
    Bridge = apps.get_model('guitars', 'Bridge')
    Brand = apps.get_model('guitars', 'Brand')
    with open('csv/bridges.csv') as file:
        file = csv.reader(file, delimiter=',')
        print(file)
        for index, data in enumerate(file):
            if index == 0:
                continue
            try:
                bridge = Bridge(
                    approved=True,
                    brand=Brand.objects.get(name=data[0]),
                    model_name=data[1],
                    origin=data[2],
                    url=data[3]
                )
                bridge.save()
            except IntegrityError:
                print(f'Bridge {bridge.model_name} already exists in database')


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0001_initial'),
        ('guitars', '0002_insert_brands')
    ]

    operations = [
        migrations.RunPython(_insert_bridges)
    ]
