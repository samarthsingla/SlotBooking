# Generated by Django 4.1 on 2022-09-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_account_is_instructor_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('student', 'Student'), ('staff', 'Staff'), ('admin', 'Admin')], max_length=20, verbose_name='Register As'),
        ),
    ]