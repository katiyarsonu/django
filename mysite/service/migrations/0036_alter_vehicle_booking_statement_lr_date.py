# Generated by Django 4.2 on 2023-06-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0035_alter_vehicle_booking_statement_pod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_booking_statement',
            name='LR_DATE',
            field=models.DateField(blank=True, null=True),
        ),
    ]
