# Generated by Django 4.1.4 on 2023-01-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('Topic_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
