# Generated by Django 2.2.3 on 2019-07-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20190711_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='identification',
            field=models.ImageField(null=True, upload_to='identification_card'),
        ),
    ]
