# Generated by Django 5.0.1 on 2024-02-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_enrollment_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='SelectMembership',
            field=models.CharField(max_length=25),
        ),
    ]
