# Generated by Django 5.0.1 on 2024-01-31 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_alter_trainer_name_alter_trainer_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
