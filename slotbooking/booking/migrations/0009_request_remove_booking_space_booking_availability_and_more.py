# Generated by Django 4.1 on 2022-09-03 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0009_alter_space_assoc_sport_alter_space_available'),
        ('booking', '0008_remove_booking_slotinfoobj_availability_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='space',
        ),
        migrations.AddField(
            model_name='booking',
            name='availability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.availability'),
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Space Name')),
                ('total_units', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('assoc_sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports.sport', verbose_name='Associated Sport')),
                ('slots', models.ManyToManyField(through='booking.Availability', to='booking.slot')),
            ],
        ),
        migrations.AlterField(
            model_name='availability',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.space'),
        ),
    ]
