# Generated by Django 4.2 on 2023-06-13 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0043_business_party_profit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Party',
        ),
        migrations.RemoveField(
            model_name='profit',
            name='business',
        ),
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='Profit',
        ),
    ]
