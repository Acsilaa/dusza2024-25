# Generated by Django 4.2.6 on 2024-11-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='joined',
            field=models.BooleanField(default=False),
        ),
    ]
