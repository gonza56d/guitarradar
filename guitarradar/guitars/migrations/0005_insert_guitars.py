import csv

from django.db import migrations, IntegrityError


def _insert_guitars(apps, schema_editor):
    Pickup = apps.get_model('guitars', 'Pickup')
    Brand = apps.get_model('guitars', 'Brand')
    Bridge = apps.get_model('guitars', 'Bridge')
    Guitar = apps.get_model('guitars', 'Guitar')
    with open('csv/guitars.csv') as file:
        file = csv.reader(file, delimiter=',')
        print(file)
        for index, data in enumerate(file):
            if index == 0:
                continue
            try:
                guitar = Guitar(
                    approved=True,
                    brand=Brand.objects.get(name=data[0]),
                    model_name=data[1],
                    url=data[2],
                    origin=data[3],
                    bridge_pickup=Pickup.objects.get(
                        brand__name=data[4].split('|')[0],
                        model_name=data[4].split('|')[1]
                    ) if data[4] else None,
                    middle_pickup=Pickup.objects.get(
                        brand__name=data[5].split('|')[0],
                        model_name=data[5].split('|')[1]
                    ) if data[5] else None,
                    neck_pickup=Pickup.objects.get(
                        brand__name=data[6].split('|')[0],
                        model_name=data[6].split('|')[1]
                    ) if data[6] else None,
                    bridge=Bridge.objects.get(
                        brand__name=data[7].split('|')[0],
                        model_name=data[7].split('|')[1]
                    ) if data[7] else None,
                    body_material=data[8],
                    neck_material=data[9],
                    fingerboard_material=data[10],
                    fingerboard_radius=data[11],
                    neck_shape=data[12],
                    strings=data[13],
                    frets_quantity=data[14],
                    frets_type=data[15],
                    scale_length=data[16],
                    pricepoint_score=data[17],
                    overall_score=data[18],
                    construction=data[19]
                )
                guitar.save()
            except IntegrityError:
                print(f'Guitar {guitar.model_name} already exists in database')


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0001_initial'),
        ('guitars', '0002_insert_brands'),
        ('guitars', '0003_insert_bridges'),
        ('guitars', '0004_insert_pickups')
    ]

    operations = [
        migrations.RunPython(_insert_guitars)
    ]
