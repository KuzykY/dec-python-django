# Generated by Django 4.0.5 on 2022-07-06 11:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel_auto_park'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]{2,100}$', 'only letters min 2 max 100 char')]),
        ),
    ]
