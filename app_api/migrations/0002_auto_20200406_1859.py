# Generated by Django 3.0.3 on 2020-04-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
