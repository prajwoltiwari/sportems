# Generated by Django 2.2.3 on 2019-07-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0006_match_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
