# Generated by Django 3.2.9 on 2022-01-11 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0005_insert_guitars'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bridge',
            options={'get_latest_by': 'created', 'ordering': ['model_name', '-modified']},
        ),
        migrations.AlterModelOptions(
            name='pickup',
            options={'get_latest_by': 'created', 'ordering': ['model_name', '-modified']},
        ),
    ]
