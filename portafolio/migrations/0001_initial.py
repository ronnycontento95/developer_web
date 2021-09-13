# Generated by Django 3.2.6 on 2021-09-13 12:27

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portafolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('url', models.TextField(max_length=500)),
                ('imagen_base', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'portafolio',
                'verbose_name_plural': 'portafolios',
            },
        ),
    ]