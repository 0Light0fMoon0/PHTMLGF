# Generated by Django 4.2.1 on 2023-06-11 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineApp', '0010_alter_portal_toplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decoration',
            name='posx',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='decoration',
            name='posy',
            field=models.FloatField(),
        ),
    ]
