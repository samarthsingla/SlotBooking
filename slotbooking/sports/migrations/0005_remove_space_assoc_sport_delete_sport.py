# Generated by Django 4.1 on 2022-08-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_rename_name_sport_sport_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='space',
            name='assoc_sport',
        ),
        migrations.DeleteModel(
            name='Sport',
        ),
    ]
