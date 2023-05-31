# Generated by Django 4.2.1 on 2023-05-26 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('body', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=300)),
            ],
        ),
    ]