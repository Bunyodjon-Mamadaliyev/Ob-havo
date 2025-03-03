# Generated by Django 5.1.6 on 2025-03-03 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_direction', models.FloatField()),
                ('precipitation', models.FloatField()),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weatherdata', to='Location.location')),
            ],
        ),
    ]
