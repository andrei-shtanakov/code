# Generated by Django 3.2.3 on 2021-07-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_alter_character_homeworld'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='height',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='mass',
            field=models.CharField(max_length=10),
        ),
    ]
