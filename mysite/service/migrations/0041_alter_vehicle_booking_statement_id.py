# Generated by Django 4.2 on 2023-06-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0040_alter_vehicle_booking_statement_billdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_booking_statement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]