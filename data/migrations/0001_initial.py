# Generated by Django 4.0 on 2022-01-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dht111',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=122)),
                ('humidity', models.CharField(max_length=122)),
                ('time',models.TimeField()),
                ('date',models.DateField()),
            ],
        ),
    ]
