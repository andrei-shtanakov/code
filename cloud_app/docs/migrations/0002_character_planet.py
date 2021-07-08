# Generated by Django 3.2.3 on 2021-07-07 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gravity', models.CharField(max_length=25)),
                ('climate', models.CharField(max_length=50)),
                ('rotation_period', models.CharField(max_length=5)),
                ('orbital_period', models.CharField(max_length=5)),
                ('diameter', models.CharField(max_length=10)),
                ('terrain', models.CharField(max_length=50)),
                ('population', models.CharField(max_length=10)),
                ('planet_id', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=5)),
                ('mass', models.CharField(max_length=5)),
                ('hair_color', models.CharField(max_length=50)),
                ('skin_color', models.CharField(max_length=50)),
                ('eye_color', models.CharField(max_length=50)),
                ('birth_year', models.CharField(max_length=10)),
                ('charact_id', models.CharField(max_length=5)),
                ('homeworld', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='docs.planet')),
            ],
        ),
    ]