# Generated by Django 4.1b1 on 2022-07-17 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodel_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ['id']},
        ),
    ]
