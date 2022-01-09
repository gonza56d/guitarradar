import csv

from django.db import migrations, IntegrityError


def _insert_pickups(apps, schema_editor):
    Pickup = apps.get_model('guitars', 'Pickup')
    Brand = apps.get_model('guitars', 'Brand')
    with open('csv/pickups.csv') as file:
        file = csv.reader(file, delimiter=',')
        print(file)
        for index, data in enumerate(file):
            if index == 0:
                continue
            try:
                pickup = Pickup(
                    brand=Brand.objects.get(name=data[0]),
                    model_name=data[1],
                    origin=data[2],
                    url=data[3],
                    active=data[4]
                )
                pickup.save()
            except IntegrityError:
                print(f'Pickup {pickup.model_name} already exists in database')


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0001_initial'),
        ('guitars', '0002_insert_brands'),
        ('guitars', '0003_insert_bridges')
    ]

    operations = [
        migrations.RunPython(_insert_pickups)
    ]
