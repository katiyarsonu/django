# Generated by Django 4.2 on 2023-06-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0036_alter_vehicle_booking_statement_lr_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_booking_statement',
            name='month',
            field=models.CharField(blank=True, choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=10, null=True),
        ),
    ]
