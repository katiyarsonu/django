# Generated by Django 4.2 on 2023-05-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_alter_vehical_expenses_advance_freight_cash_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehical_expenses',
            name='Date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehical_expenses',
            name='LR_DATE',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehical_expenses',
            name='NEFT_Date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehical_expenses',
            name='POD_Rcv_Dt',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehical_expenses',
            name='Placement_Date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
