# Generated by Django 3.2.3 on 2021-07-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_auto_20210708_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='charact_url',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AlterField(
            model_name='planet',
            name='orbital_period',
            field=models.CharField(max_length=99),
        ),
        migrations.AlterField(
            model_name='planet',
            name='planet_url',
            field=models.CharField(default='', max_length=99),
        ),
        migrations.AlterField(
            model_name='planet',
            name='rotation_period',
            field=models.CharField(max_length=99),
        ),
    ]