# Generated by Django 4.2.1 on 2023-05-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_card_no_customer_meter_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='details',
        ),
        migrations.AddField(
            model_name='customer',
            name='units',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
