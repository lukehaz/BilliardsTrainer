# Generated by Django 4.2.5 on 2023-10-01 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_stats_aces_remove_stats_iswinner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='drillPercent',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='totalDrills',
        ),
    ]
