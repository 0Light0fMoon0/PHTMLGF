# Generated by Django 4.2.1 on 2023-05-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineApp', '0002_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='posx',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='building',
            name='posy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='posx',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='posy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='water',
            name='posx',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='water',
            name='posy',
            field=models.FloatField(),
        ),
    ]
