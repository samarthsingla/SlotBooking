# Generated by Django 4.1 on 2022-09-01 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0008_space_slots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='assoc_sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.sport', verbose_name='Associated Sport'),
        ),
        migrations.AlterField(
            model_name='space',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]